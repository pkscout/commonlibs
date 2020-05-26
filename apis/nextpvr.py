#v.0.1.2

from . import url

JSONURL = url.URL( 'json' )



class API( object ):

    def __init__( self, dvr_host, dvr_port, dvr_auth ):
        url_end = 'services/service'
        self.BASEURL = 'http://%s:%s/%s' % (dvr_host, dvr_port, url_end)
        self.PINCODE = dvr_auth
        self.PARAMS = {}
        self.PARAMS['format'] = 'json'
        self.PARAMS['sid'] = ''


    def searchForEpisode( self, name ):
        params = self.PARAMS
        params['method'] = 'channel.listings.search'
        params['title'] = name
        return self._do_call( params )


    def getRecordingList( self, recording_id='', filter='' ):
        params = self.PARAMS
        params['method'] = 'recording.list'
        if recording_id:
            params['recording_id'] = recording_id
        elif filter:
            params['filter'] = filter
        else:
            params['filter'] = 'all'
        return self._do_call( params )


    def getScheduledRecordings( self ):
        params = self.PARAMS
        params['method'] = 'recording.recurring.list'
        return self._do_call( params )


    def scheduleNewRecurringRecording( self, name, params={} ):
        loglines = []
        success, t_loglines, results = self.searchForEpisode( name )
        loglines.extend( t_loglines )
        if not success:
            loglines.append( 'no listings found for %s, skipping' % name )
            return False, loglines, []
        listings = results.get( 'listings', [] )
        params.update( self.PARAMS )
        params['method'] = 'recording.recurring.save'
        for listing in listings:
            if listing.get( 'name' ) == name:
                params['event_id'] = listing.get( 'id' )
                loglines.append( 'found matching listing for %s' % name )
                success, t_loglines, results = JSONURL.Get( self.BASEURL, params=params )
                loglines.extend( t_loglines )
                return True, loglines, results
            else:
                loglines.append( 'no match between listing %s and name %s' % (listings.get( 'name' ), name) )
        return False, loglines, []

    def _do_call( self, params ):
        loglines = []
        if not params['sid']:
            success, t_loglines = self._login()
            loglines.extend( t_loglines )
            if not success:
                return False, loglines, []
            params['sid'] = self.PARAMS['sid']
        success, t_loglines, results = JSONURL.Get( self.BASEURL, params=params )
        loglines.extend( t_loglines )
        if success and results:
            return success, loglines, results
        else:
            return False, loglines, []


    def _login( self ):
        params = { 'format':'json' }
        params['method'] = 'session.initiate'
        params['ver'] = '1.0'
        params['device'] = 'tvmaze.integration'
        success, loglines, keys = JSONURL.Get( self.BASEURL, params=params )
        if success:
            sid = keys['sid']
            salt = keys['salt']
            params = { 'format':'json' }
            params['sid'] = sid
            params['method'] = 'session.login'
            params['md5'] = self._hash_me( ':' + self._hash_me( self.PINCODE ) + ':' + salt )
            success, a_loglines, login = JSONURL.Get( self.BASEURL, params=params )
            loglines.extend( a_loglines )
            if success and login['stat'] == 'ok':
                self.PARAMS['sid'] = login['sid']
                return True, loglines
            else:
                loglines.append( 'unable to login' )
                return False, loglines
        else:
            loglines.append( 'unable to login' )
            return False, loglines


    def _hash_me ( self, thedata ):
        import hashlib
        h = hashlib.md5()
        h.update( thedata.encode( 'utf-8' ) )
        return h.hexdigest()
