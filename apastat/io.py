from urllib2 import urlopen


def get_document(url):
    return urlopen(url).read()
