import re

def isValidURL(url):
    regex = ("((http|https)://)(www.)?" +
        "[a-zA-Z0-9@:%._\\+~#?&//=]" +
        "{2,256}\\.[a-z]" +
        "{2,6}\\b([-a-zA-Z0-9@:%" +
        "._\\+~#?&//=]*)")
    if url:
        if re.search(regex,url):
            return True
        else:
            return False
    else:
        return False

	