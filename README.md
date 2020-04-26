# pkscout's common libraries

A collection of some of the common libraries I use across Python projects.  Most of the functions in these projects all work with both Python3 and the Python interpreter built into [Kodi](http://kodi.tv).  The notable exception is kodisettings.py which, predictably, only works in Kodi.
 
## ---fileops.py---

### checkPath( thepath, createdir=True )
Checks to see if path exists. If the path does not exist, by default it is created.  
* **Required**  
`thepath` (`<string>`)  

* **Optional**  
`createdir = <boolean>` (default `True`)  

* **Returns**  
`<tuple>` of `(<boolean> of path existence, <array> of debug loglines)`

* **Notes**  
If using in Kodi, the path must end in the directory separator. To do that try: `os.path.join( 'this', 'is', 'thepath', '' )`

### copyFile( thesource, thedest )
Copies a file from source to destination.

* **Required**  
`thesource` (`<string>`)  
`thedest` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<boolean> of copied status, <array> of debugloglines)`

### deleteFile( thesource )
Deletes a file.

* **Required**  
`thesource` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<boolean> of deleted status, <array> of debugloglines)`

### deleteFolder( thesource )
Deletes a folder (including all contents).

* **Required**  
`thesource` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<boolean> of deleted status, <array> of debugloglines)`

### moveFile( thesource, thedest )
Moves a file from source to destination. Note that for maximum compatibility this works by copying the file to the destination and then deleting the file from the source.

* **Required**  
`thesource` (`<string>`)  
`thedest` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<boolean> of moved status, <array> of debugloglines)`

### naturalKeys( thelist )
Sorts a list in "natural" order. For instance 1,10,2,3,4,5,6,7,8,9 would be sorted to 1,2,3,4,5,6,7,8,9,10.

* **Required**  
`thelist` (`<list of strings.  

* **Returns:**  
`<list>`

### osPathFromString( spath, sep='/' )
Returns filesystem specific path from a string. Note that regardless of platform, the path should be POSIX style (unless you change the default `sep`). So on Windows it would be `/C:/Path/to/video/source`

* **Required**  
`spath` (`<string>`)  

* **Optional**  
`sep` (`<string>`): default is `'/'`

* **Returns:**  
`<os path object>`

### readFile( filename )
Reads a file (full path required). The type of data returned will depend on the file read.  Apologies that the returned values for this one don't conform to the standard where the loglines are returned second. It's too much of a hassle to change it now.

* **Required**  
`filename` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<array> of debug lines, contents of file)`

### renameFile ( thesource, thedest )
Renames a file.  This is a move in the traditional sense, but note that in Kodi this only works if the source and destination file systems aren't the same. I suggest you try this and if it fails then fall back to moveFile.

* **Required**  
`thesource` (`<string>`)  
`thedest` (`<string>`)  

* **Returns:**  
`<tuple>` of `(<boolean> of renamed status, <array> of debugloglines)`

### writeFile( data, filename, wtype='wb' )
Writes data to a file.  By default it writes binary data, but you can change wtype to 'w' to write string or unicode data.

* **Required**  
`data` (either `<binary>` or `<string/unicode>`)  
`filename` (`<string>`)  

* **Optional**  
`wtype` (`<string>`): default is `'wb'`

* **Returns:**  
`<tuple>` of `(<boolean> of write status, <array> of debugloglines)`

## ---kodisettings.py---

### getSettingBool( addon, setting_name, default=False )
Gets a Kodi boolean setting and returns it as a Python boolean. If the setting is not found or there is a problem converting to a boolean, returns the default value.

* **Required**  
`addon` (`<an xbmcaddon.Addon() object>`)  
`setting_name` (`<string>`)  

* **Optional**  
`default` (`<boolean>`): default is `False`  

* **Returns:**  
boolean

### getSettingInt( addon, setting_name, default=0 )
Gets a Kodi integer setting and returns it as a Python integer. If the setting is not found or there is a problem converting to an integer, returns the default value.

* **Required**  
`addon` (`<an xbmcaddon.Addon() object>`)  
`setting_name` (`<string>`)  

* **Optional**  
`default` (`<int>`): default is `0`

* **Returns:**  
<int>

### getSettingNumber( addon, setting_name, default=0.0 )
Gets a Kodi numeric setting and returns it as a Python float. If the setting is not found or there is a problem converting to a float, returns the default value.

* **Required**  
`addon` (`<an xbmcaddon.Addon() object>`)  
`setting_name` (`<string>`)  

* **Optional**  
`default` (`<float>`): default is `0.0`  

* **Returns:**  
`<float>`

### getSettingString( addon, setting_name, default='' )
Gets a Kodi setting and returns it as a Python string. If the setting is not found or there is a problem converting to a string, returns the default value.

* **Required**  
`addon` (`<an xbmcaddon.Addon() object>`)  
`setting_name` (`<string>`)  

* **Optional**  
`default` (`<string>`): default is `''`

* **Returns:**  
`<string>`

## ---transforms.py---

### getImageType( filename )
Determines the type of image and returns the valid extension for that image type (including the dot).

* **Required**  
`filename` (`<string>`)  

* **Returns:**  
`<string>`

### replaceWords( text, word_dict )
Takes a string and replaces words based on the word_dict.

* **Required**  
`text` (`<string>`)  
`word_dict` (`<dict>`)  

```python
        word_dict = {
            'badword': 'replacement',
            'another' : 'thisinstead' }
```

* **Returns:**  
`<string>`

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

* **Optional**  
`returntype` (`<string>`): default is `'text'` with options for `'json'` or `'binary'`  
`headers` (`<dict>`): default is `{}`. When including headers should be paired by `name:value` in the `<dict>`  
timeout (`<int>`): default is `10`. This is the amount of time (in seconds) before the object should give up trying to communicate with the remote site

### Interacting with sites
The URL has three methods: Get, Post, and Delete. As an example:

```python
    returnedData = myURL.Get( 'https://www.apple.com' )
```

* **Get( url, params={}, data='' )**

* **Required**  
`url` (`<string>`)  

* **Optional**  
`params` (`<dict>`): default is `{}`. When passed paramaters will be parsed out as `name:value`, url encoded, and sent as part of the URL.  
data: (`<string>`): default is `''`. When passed, data will be url encoded and sent as part of the URL)

* **Post( url, params={}, data='' )**

* **Required**  
`url` (`<string>`)  

* **Optional**  
`params` (`<dict>`): default is `{}`. When passed paramaters will be parsed out as `name:value` and sent as part of the post request.  
data: (`<string>`): default is `''`. When passed, data will be url encoded and sent as part of the post request)

* **Delete( url, params={}, data='' )**

* **Required**  
`url` (`<string>`)  

* **Optional**  
`params` (`<dict>`): default is `{}`. When passed paramaters will be parsed out as `name:value` and sent as part of the delete request.  
data: (`<string>`): default `''`. When passed, data will be url encoded and sent as part of the delete request)

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

* **Optional**  
`preamble` (`<string>`): default is `''`. To help you find things in the Kodi log, it's recommended that you prepend a string to identify your addon in the log. For instance, Artist Slideshow uses a preamble of `'[Artist Slideshow] '`.  
`logdebug` (`<boolean>`): default is `False`. To keep Kodi debug logs cleaner, addons are asked to have a setting to enable debug logging for the addon (so that every addon isn't dumping debug information into the log at the same time). By default the Logger class will not log items set to `xbmc.LOGDEBUG` unless an addon setting is passed in with a boolean value of `True`.

### Logging information in Kodi

```python
    myLogger.log( loglines )
```

* **Required**  
`loglines` (`<list>`). This is a list of lines you want sent to the log (even if it's just one line, it **MUST** be in a list).  

* **Optional**  
`loglevel` (`<xbmc loglevel object>`): default is `xbmc.LOGDEBUG`. Other levels you can use are `xbmc.LOGINFO`, `xbmc.LOGWARNING`, `xbmc.LOGERROR`, `xbmc.LOGFATAL`.

### Creating a Logger for Python scripts

```python
    myLogger = Logger()
```

* **Optional**  
`logconfig` (`<string>`): default is `'timed'`. If set for `'timed'`, logs are rotated daily at midnight. If set to `'rotating'`, logs are rolled after the log reaches a certain size.  
`maxsize` (`<int>`): default is `100000`. If using rotating logs, size in bytes when the log will roll.  
`numbackups` (`<int`>): default is `5`. The number of rolled log files that will be kept.  
`logfile` (`<string`>): default is `logfile.log`. This is the path to the logfile you want to create. If you include only a file name, it will be saved in the same directory as the script running it.  
`preamble` (`<string`>): default is `''`. This is the string you want prepended to each log line.  
`logformat` (`<string`>): default is `'%(asctime)-15s %(levelname)-8s %(message)s'`. See [logging.Formater documentation](https://docs.python.org/3/library/logging.html#logging.Formatter) for details on options.  
`logdebug` (`<boolean`>): default is `False`. Set to True if you want DEBUG level events logged. This lets you have a setting in your script to enable or disable debug logging.  

### Logging information in a Python script

```python
    myLogger.log( loglines )
```

* **Required**  
`loglines` (`<list>`). This is a list of lines you want sent to the log (even if it's just one line, it **MUST** be in a list).  

* **Optional**  
`loglevel` (`<string>`): default is `'debug'`. Other levels are `'info'`, `'warning'`, `'error'`, and `'critical'`.

