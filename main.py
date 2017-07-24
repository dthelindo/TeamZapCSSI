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
    location = ndb.StringProperty()
    

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
