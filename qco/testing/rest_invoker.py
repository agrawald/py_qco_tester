import urllib2


def get(url):
    return urllib2.urlopen(url).read()


def post(url, params):
    return urllib2.urlopen(url, params).read()
