import os
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from models import user_model, ev_datastore
from add_ev import AddEV
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'], autoescape = True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        user = users.get_current_user()

        if user:
            url = users.create_logout_url('/')
            url_string = 'logout'
            myuser_key = ndb.Key('user_model', user.user_id())
            myuser = myuser_key.get()

            if myuser == None:
                myuser = user_model(id = user.user_id())
                myuser.username = user.email()
                myuser.put()

        else:
            url = users.create_login_url('/')
            url_string = 'login'

        template_values = { 
            'url': url,
            'url_string': url_string,
            'user': user
            }

        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication(
    [('/', MainPage),
    ('/add_ev', AddEV),
    ], 
    debug=True)
