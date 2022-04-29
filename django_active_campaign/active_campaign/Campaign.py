from ActiveCampaign import ActiveCampaign
import simplejson as json
import urllib2, urllib
import datetime, time

class Campaign(ActiveCampaign):

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        ActiveCampaign.__init__(self, url, api_key)

    def create(self, params, post_data):
        request_url = '%s&api_action=campaign_create&api_output=%s' % (self.url, self.output)
        post_data = urllib.urlencode(post_data)
        req = urllib2.Request(request_url, post_data)
        response = json.loads(urllib2.urlopen(req).read())
        return response

    def delete(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_delete&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def delete_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_delete_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def list_(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def paginator(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_paginator&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
    
    def report_bounce_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_bounce_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_bounce_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_bounce_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_forward_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_forward_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_forward_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_forward_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_link_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_link_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_link_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_link_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_open_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_open_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_open_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_open_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unopen_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unopen_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unsubscription_list(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unsubscription_list&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def report_unsubscription_totals(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_report_unsubscription_totals&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def send(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_send&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response

    def status(self, params, post_data = {}):
        request_url = '%s&api_action=campaign_status&api_output=%s&%s' % (self.url, self.output, params)
        response = json.loads(urllib2.urlopen(request_url).read())
        return response
