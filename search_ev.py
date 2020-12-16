import os
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from models import user_model, ev_datastore

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'], autoescape=True)


class SearchEV(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        url = users.create_logout_url('/')
        url_string = 'Logout'
        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
            'action': 'Search'
        }
        template = JINJA_ENVIRONMENT.get_template('search_ev.html')
        self.response.write(template.render(template_values))
