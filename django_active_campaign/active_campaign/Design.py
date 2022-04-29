import json
import urllib2, urllib

from ActiveCampaign import ActiveCampaign

class Design(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def edit(self, params, post_data):
        request_url = '%s&api_action=branding_edit&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response
        
    def view(self, params, post_data):
        request_url = '%s&api_action=branding_view&api_output=%s' % (self.url, self.output)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
