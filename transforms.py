#v.0.3.2

import imghdr, re


def getImageType( filename ):
    try:
        new_ext = '.' + imghdr.what( filename ).replace( 'jpeg', 'jpg' )
    except Exception:
        new_ext = '.tbn'
    return new_ext

def replaceWords( text, word_dic ):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile( '|'.join( map( re.escape, word_dic ) ) )
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)
