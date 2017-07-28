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
api_key = "AIzaSyD6eVuPTwr53NoO6fp1WhFor5a4m6SuimY"

'''
class Trip(ndb.Model):
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    date = ndb.DateProperty()
'''

class Login(ndb.Model):
    user_email = ndb.StringProperty()


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

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "Dubai"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]

            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("dubai.html")
        self.response.out.write(template.render(my_vars))

class HongKongHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "Hong Kong"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]

            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("hongkong.html")
        self.response.out.write(template.render(my_vars))

class IcelandHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "iceland"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)

        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]

            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("iceland.html")
        self.response.out.write(template.render(my_vars))

class MaldivesHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "maldives"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]


            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("maldives.html")
        self.response.out.write(template.render(my_vars))

class MexicoCityHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "mexicocity"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]


            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("mexicocity.html")
        self.response.out.write(template.render(my_vars))

class NewZealandHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "auckland"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]


            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("newzealand.html")
        self.response.out.write(template.render(my_vars))

class SantoriniHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "santorini"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]


            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("santorini.html")
        self.response.out.write(template.render(my_vars))

class CanadaHandler(webapp2.RequestHandler):
    def get(self):

        interest = self.request.get("interest")
        city = self.request.get("city")

        if not interest:
            interest = "Hotels"

        if not city:
            city = "Vancouver"

        params = {
                    "query" : interest+"in"+city,
                    "height" : 853,
                    "width" : 1280,
                    "key": api_key,
                  }

        query_text = urllib.urlencode(params)
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?" + query_text

        address_response = urllib2.urlopen(api_url)
        content = address_response.read()
        content_dict = json.loads(content)


        places_list = []
        placescount = 0
        photo = ''

        for item in content_dict["results"]:
            photo_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&key="+api_key+"&photoreference=" + item["photos"][0]["photo_reference"]
            place_list = [ item["name"], item["formatted_address"], photo_url]


            placescount += 1
            if placescount < 6:
                places_list.append(place_list)

        my_vars = {
                    "places_list": places_list,
                  }
        template = env.get_template("canada.html")
        self.response.out.write(template.render(my_vars))

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
    ('/canada', CanadaHandler),
    ('/team', TeamHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler),
], debug=True)
