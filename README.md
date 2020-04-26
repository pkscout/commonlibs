# pkscout's common libraries

A collection of some of the common libraries I use across Python projects.  Most of the functions in these projects all work with both Python3 and the Python interpreter built into [Kodi](http://kodi.tv).  The notable exception is kodisettings.py which, predictably, only works in Kodi.
 
## ---fileops.py---

### checkPath( thepath, createdir=True )
Checks to see if path exists. If the path does not exist, by default it is created.

**Required**<br />
thepath: string<br />
**Optional**<br />
createdir: boolean (default True)<br />
**Returns:**<br />
tuple of (boolean of path existence, array of debug loglines)

### copyFile( thesource, thedest )
Copies a file from source to destination.

**Required**<br />
thesource: string<br />
thedestination: string<br />
**Returns:**<br />
tuple of (boolean of copied status, array of debug loglines)

### deleteFile( thesource )
Deletes a file.

**Required**<br />
thesource: string<br />
**Returns:**<br />
tuple of (boolean of deleted status, array of debug loglines)

### deleteFolder( thesource )
Deletes a folder (including all contents).

**Required**<br />
thesource: string<br />
**Returns:**<br />
tuple of (boolean of deleted status, array of debug loglines)

### moveFile( thesource, thedest )
Moves a file from source to destination. Note that for maximum compatibility this works by copying the file to the destination and then deleting the file from the source.

**Required**<br />
thesource: string<br />
thedest: string<br />
**Returns:**<br />
tuple of (boolean of moved status, array of debug loglines)

### naturalKeys( thelist )
Sorts a list in "natural" order. For instance 1,10,2,3,4,5,6,7,8,9 would be sorted to 1,2,3,4,5,6,7,8,9,10.

**Required**<br />
thelist: list of strings<br />
**Returns:**<br />
list

### osPathFromString( spath)
Returns filesystem specific path from a string

**Required**<br />
spath: string - regardless of platform, the path should be POSIX style. So on Windows it would be `/C:/Path/to/video/source`<br />
**Optional**<br />
sep: string (default '/') - if you want to use a different separator for the input string<br />
**Returns:**<br />
os path object

### readFile( filename )
Reads a file (full path required). The type of data returned will depend on the file read.  Apologies that the returned values for this one don't conform to the standard where the loglines are returned second. It's too much of a hassle to change it now.

**Required**<br />
filename: string<br />
**Returns:**<br />
tuple of (array of debug lines, contents of file)

### renameFile ( thesource, thedest )
Renames a file.  This is a move in the traditional sense, but note that in Kodi this only works if the source and destination file systems aren't the same. I suggest you try this and if it fails then fall back to moveFile.

**Required**<br />
thesource: string<br />
thedest: string<br />
**Returns:**<br />
tuple of (boolean of renamed status, array of debug loglines)

### writeFile( data, filename, wtype='wb' )
Writes data to a file.  By default it writes binary data, but you can change wtype to 'w' to write text.

**Required**<br />
data: either binary or string/unicode<br />
filename: string<br />
**Optional**<br />
wtype: string (default 'wb') - use 'w' to write string or unicode data<br />
**Returns:**<br />
tuple of (boolean of write status, array of debug loglines)

## ---kodisettings.py---

### getSettingBool( addon, setting_name, default=False )
Gets a Kodi boolean setting and returns it as a Python boolean. If the setting is not found or there is a problem converting to a boolean, returns the default value.

**Required**<br />
addon: an xbmcaddon.Addon() object<br />
setting_name: string<br />
**Optional**<br />
default: boolean (default False)<br />
**Returns:**<br />
boolean

### getSettingInt( addon, setting_name, default=0 )
Gets a Kodi integer setting and returns it as a Python integer. If the setting is not found or there is a problem converting to an integer, returns the default value.

**Required**<br />
addon: an xbmcaddon.Addon() object<br />
setting_name: string<br />
**Optional**<br />
default: int (default 0)<br />
**Returns:**<br />
integer

### getSettingNumber( addon, setting_name, default=0.0 )
Gets a Kodi numeric setting and returns it as a Python float. If the setting is not found or there is a problem converting to a float, returns the default value.

**Required**<br />
addon: an xbmcaddon.Addon() object<br />
setting_name: string<br />
**Optional**<br />
default: float (default 0.0)<br />
**Returns:**<br />
float

### getSettingString( addon, setting_name, default='' )
Gets a Kodi setting and returns it as a Python string. If the setting is not found or there is a problem converting to a string, returns the default value.

**Required**<br />
addon: an xbmcaddon.Addon() object<br />
setting_name: string<br />
**Optional**<br />
default: string (default '')<br />
**Returns:**<br />
string

## ---transforms.py---

### getImageType( filename )
Determines the type of image and returns the valid extension for that image type (including the dot).

**Required**<br />
filename: string<br />
**Returns:**<br />
string

### replaceWords( text, word_dict )
Takes a string and replaces words based on the word_dict.

**Required**<br />
text: string<br />
word_dict: dict<br />

```python
    word_dict = {
        'badword': 'replacement',
        'another' : 'thisinstead' }
```
**Returns:**<br />
string

## ---url.py---
This class is a wrapper for the requests module to make it easier to create URLs to get back data and binary objects from web sites.

### Importing the URL class

```python
    from url import URL
```

### Creating a URL object

```python
    myURL = URL( returntype='text', headers={}, timeout=10 )
```

**Optional**<br />
returntype: string (default 'text' with options for 'json' or 'binary')<br />
headers: dict (default {}) - headers should be paired by name:value in the dict<br />
timeout: int (default 10) - the amount of time before the object should give up trying to communicate with the remote site

### Interacting with sites
The URL has three methods: Get, Post, and Delete. As an example:

```python
    returnedData = myURL.Get( 'https://www.apple.com' )
```

**Get( url, params={}, data='' )**

**Required**<br />
url: string<br />
**Optional**<br />
params: dict (paramaters will be parsed out as name:value, url encoded, and sent as part of the URL)<br />
data: string (data will be url encoded and sent as part of the URL)

**Post( url, params={}, data='' )**

**Required**<br />
url: string<br />
**Optional**<br />
params: dict (paramaters will be parsed out as name:value, and sent as part of the post request)<br />
data: string (data will be url encoded and sent as part of the post request)

**Delete( url, params={}, data='' )**

**Required**<br />
url: string<br />
**Optional**<br />
params: dict (paramaters will be parsed out as name:value, and sent as part of the delete request)<br />
data: string (data will be url encoded and sent as part of the delete request)

## ---xlogger.py---
This class is a wrapper for the Kodi logger or Python logging class (depending on the context in which you use it).

### Importing the Logger class

```python
    from xlogger import Logger
```

### Creating a Logger object for Kodi

```python
    myLogger = Logger()
```

**Optional**<br />
preamble: string (default '') - To help you find things in the Kodi log, it's recommended that you prepend a string to identify your addon in the log. For instance, Artist Slideshow uses a preamble of '[Artist Slideshow] '.<br />
logdebug: boolean (default False) - To keep Kodi debug logs cleaner, addons are asked to have a setting to enable debug logging for the addon (so that every addon isn't dumping debug information into the log at the same time). By default the Logger class will not log items set to xbmc.LOGDEBUG unless an addon setting is passed in with a boolean value of True.

### Logging information in Kodi

```python
    myLogger.log( loglines )
```

**Required**<br />
loglines: list - a list of lines you want sent to the log (even if it's just one line, it **MUST** be in a list)<br />
**Optional**<br />
loglevel: xbmc loglevel object (default xbmc.LOGDEBUG) - other levels are xbmc.LOGINFO, xbmc.LOGWARNING, xbmc.ERROR, xbmc.FATAL.

### Creating a Logger for Python scripts

```python
    myLogger = Logger()
```

**Optional**<br />
logconfig: string (default: 'timed') - If set for timed, logs are rotated daily at midnight. If set to 'rotating, logs are rolled after the log reaches a certain size.<br />
maxsize: int (default 100000) - if using rotating logs, size in bytes when the log will roll.<br />
numbackups: int (default 5) - the number of rolled log files that will be kept. <br />
logfile: string (default logfile.log) - path to the logfile you want to create. If you include only a file name, it will be saved in the same directory as the script running it.<br />
preamble: string (default '') - the string you want prepended to each log line<br />
logformat: string (default '%(asctime)-15s %(levelname)-8s %(message)s') - see [logging.Formater documentation](https://docs.python.org/3/library/logging.html#logging.Formatter) for details on options.<br />
logdebug: boolean (default False) - set to True if you want DEBUG level events logged. This lets you have a setting in your script to enable or disable debug logging.<br />

### Logging information in a Python script

```python
    myLogger.log( loglines )
```

**Required**<br />
loglines: list - a list of lines you want sent to the log (even if it's just one line, it **MUST** be in a list)<br />
**Optional**<br />
loglevel: string (default 'debug') - other levels are 'info', 'warning', 'error', and 'critical'














