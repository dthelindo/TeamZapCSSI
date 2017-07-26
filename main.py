from google.appengine.api import users
from google.appengine.ext import ndb
import datetime
import jinja2
import json
import logging
import os
import pprint
import urllib
import urllib2
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

'''
class Trip(ndb.Model):
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    date = ndb.DateProperty()
'''

class Login(ndb.Model):
    user_email = ndb.StringProperty()
    #password = ndb.StringProperty()


class MainHandler(webapp2.RequestHandler):
    def get(self):
        cur_user = users.get_current_user()
        name = None
        if cur_user:
            log_url = users.create_logout_url('/')
            name = cur_user.nickname().split('@')[0]
        else:
            log_url = users.create_login_url('/')
        template = env.get_template('main.html')

        login = None
        if cur_user:
            login_key = ndb.Key('Login', cur_user.nickname())
            login = login_key.get()

            if not login:
                login = Login(
                        user_email = cur_user.nickname()
                )
            login.key = login_key
            login.put()

        variables = {
            'user': cur_user,
            'log_url': log_url,
            'login': login,
            'name': name,
        }
        self.response.out.write(template.render(variables))

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
        cur_user = users.get_current_user()
        if cur_user:
            key = ndb.Key('Login', self.request.get('email'))
            user = key.get()
            if not user:
                    user = Login(user_email=key)
                    user.key = key
            user.put()

        template = env.get_template("login.html")
        self.response.out.write(template.render())

class DubaiHandler(webapp2.RequestHandler):
    def get(self):

        template = env.get_template("dubai.html")

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Attractions"

        if not city:
            city = "Dubai"

        params = {
                    "query" : interest+"in"+city,
                    "key": "AIzaSyAd_wleTmel1WiMaeVNaDjc1-pPjEQV0Mg",
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0

        for item in content_dict["results"]:
            place_list = [ item["name"], item["formatted_address"]]

            placescount += 1
            if placescount < 11:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }

        self.response.out.write(template.render(my_vars))

class HongKongHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("hongkong.html")

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Attractions"

        if not city:
            city = "Hong Kong"

        params = {
                    "query" : interest+"in"+city,
                    "key": "AIzaSyAd_wleTmel1WiMaeVNaDjc1-pPjEQV0Mg",
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0

        for item in content_dict["results"]:
            place_list = [ item["name"], item["formatted_address"]]

            placescount += 1
            if placescount < 11:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }

        self.response.out.write(template.render(my_vars))

class IcelandHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("iceland.html")

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Attractions"

        if not city:
            city = "icealand"

        params = {
                    "query" : interest+"in"+city,
                    "key": "AIzaSyAd_wleTmel1WiMaeVNaDjc1-pPjEQV0Mg",
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0

        for item in content_dict["results"]:
            place_list = [ item["name"], item["formatted_address"]]

            placescount += 1
            if placescount < 11:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }

        self.response.out.write(template.render(my_vars))

class MaldivesHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("maldives.html")

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Attractions"

        if not city:
            city = "maldives"

        params = {
                    "query" : interest+"in"+city,
                    "key": "AIzaSyAd_wleTmel1WiMaeVNaDjc1-pPjEQV0Mg",
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0

        for item in content_dict["results"]:
            place_list = [ item["name"], item["formatted_address"]]

            placescount += 1
            if placescount < 11:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }

        self.response.out.write(template.render(my_vars))

class MexicoCityHandler(webapp2.RequestHandler):
    def get(self):
        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Attractions"

        if not city:
            city = "mexico city"
#To set a default you will need an "if not" statement


        params = {
                    "query" : interest+"in"+city,
                    "key": "AIzaSyAd_wleTmel1WiMaeVNaDjc1-pPjEQV0Mg",
                }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        #Line 21 is used as to log the whole url query

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0


        for item in content_dict["results"]:
            place_list = [ item["name"], item["formatted_address"]]

            placescount += 1
            if placescount < 11:
                places_list.append(place_list)

        my_vars = {

            "places_list": places_list,
            #"fotos_list": fotos_list,
        }

        template = env.get_template("mexicocity.html")

        self.response.out.write(template.render(my_vars))

class NewZealandHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("newzealand.html")
        self.response.out.write(template.render())

class SantoriniHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("santorini.html")
        self.response.out.write(template.render())

class TeamHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("team.html")
        self.response.out.write(template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("about.html")
        self.response.out.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("contact.html")
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
    ('/login', LoginHandler),
    ('/dubai', DubaiHandler),
    ('/hongkong', HongKongHandler),
    ('/iceland', IcelandHandler),
    ('/maldives', MaldivesHandler),
    ('/mexicocity', MexicoCityHandler),
    ('/newzealand', NewZealandHandler),
    ('/santorini', SantoriniHandler),
    ('/team', TeamHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler),
], debug=True)
