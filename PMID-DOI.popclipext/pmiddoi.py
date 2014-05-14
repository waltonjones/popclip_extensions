import os
import urllib2
import json
import sys

input = os.environ['POPCLIP_TEXT']

request = urllib2.Request("http://pmid2doi.labs.crossref.org/" + input, headers={"Accept": "application/json"})
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print 'Could not locate paper ID.'
    print 'Error code: ', e.code,
except urllib2.URLError, e:
    print 'We failed to reach the server.'
    print 'Reason: ', e.reason,
else:
    response = json.loads(response.read())
    if "/" in input:
        sys.stdout.write(str(response['mapping']['pmid']))
    else:
        sys.stdout.write(str(response['mapping']['doi']))