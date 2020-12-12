from google.appengine.ext import ndb

class user_model(ndb.Model):
    username = ndb.StringProperty()