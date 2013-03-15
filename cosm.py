"""
API for COSM.com
"""
import urllib2

def submit_datapoints(feed,datastream,key,csv):
    """
    Submit CSV-formatted list of datapoints to specified datastream
    """
    if len(csv)==0:
        return
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request("http://api.cosm.com/v2/feeds/%s/datastreams/%s/datapoints.csv" % (feed,datastream), csv)
    request.add_header('Host','api.cosm.com')
    request.add_header('Content-type','text/csv')
    request.add_header('X-ApiKey', key)
    opener.open(request)
