#TODO Dainel: Create login, handlers, etc
from google.appengine.api import users
from google.appengine.ext import ndb
import datetime
import jinja2
import json
import logging
import os
import urllib
import urllib2
import webapp2

class Trip(ndb.Model):
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    date = ndb.DateProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        log_url = ''
        if cur_user:
            log_url = users.create_logout_url('/')
        else:
            log_url = users.create_login_url('/')
        search_term = self.request.get('q')

        template = env.get_template('main.html')
        variables = {
            'user': cur_user,
            'log_url': log_url,
        }

class FlightHandler(webapp2.RequestHandler):
    def post(self):
        response = urllib2.urlopen('http://jservice.io/api/random')
        content = response.read()
        content_dict = json.loads(content)

        child_passengers = content_dict['request']['passengers']['childCount']
        adult_passengers = content_dict['request']['passengers']['adultCount']
        senior_passengers = content_dict['request']['passengers']['seniorCount']

        destination = content_dict['slice']['destination']

class SurveyHandler(webapp2.RequestHandler):
    def get(self):


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/survey', SurveyHandler),
    ('/trips', TripHandler),
    ('/get_flight', FlightHandler),
    ('/get_attractions', AttractionHandler),
], debug=True)
