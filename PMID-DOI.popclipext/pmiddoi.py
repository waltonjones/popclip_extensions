import os
import urllib2
import json

# input = os.environ['POPCLIP_TEXT']
input = "10.1371/journal.pgen.1001346"


request = urllib2.Request("http://pmid2doi.labs.crossref.org/" + input, headers={"Accept": "application/json"})
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print 'That ID is not the database. :('
    print 'Error code: ', e.code
except urllib2.URLError, e:
    print 'We failed to reach the server.'
    print 'Reason: ', e.reason
else:
    response = response.read()
    response_dict = json.loads(response)
    if "/" in input:
        print(response_dict['mapping']['pmid'])
    else:
        print(response_dict['mapping']['doi'])
