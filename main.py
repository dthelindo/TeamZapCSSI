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

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class Trip(ndb.Model):
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    date = ndb.DateProperty()

class Login(ndb.Model):
    user_email = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        '''log_url = ''
        if cur_user:
            log_url = users.create_logout_url('/')
        else:
            log_url = users.create_login_url('/')
        search_term = self.request.get('q')
'''
        template = env.get_template('main.html')
        variables = {
            'user': cur_user,
            #'log_url': log_url,
        }
        self.response.out.write(template.render(variables))

''' class FlightHandler(webapp2.RequestHandler):
    def post(self):
        response = urllib2.urlopen('https://www.googleapis.com/qpxExpress/v1/trips/search')
        content = response.read()
        content_dict = json.loads(content)

        child_passengers = content_dict['request']['passengers']['childCount']
        adult_passengers = content_dict['request']['passengers']['adultCount']
        senior_passengers = content_dict['request']['passengers']['seniorCount']

        destination = content_dict['request']['slice']['destination']'''

class SurveyHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("survey.html")
        self.response.out.write(template.render())

    def post(self):
        my_vars = {
            'landscape': landscape
        }
        template = env.get_template("results.html")
        self.response.out.write(template.render(my_vars))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("login.html")
        self.response.out.write(template.render())
'''
class TripHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("trips.html")
        self.response.out.write(template.render())

class AttractionHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("attractions.html")
        self.response.out.write(template.render())
'''

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/survey', SurveyHandler),
    ('/login', LoginHandler)
], debug=True)
