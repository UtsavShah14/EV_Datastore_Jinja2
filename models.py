from google.appengine.ext import ndb

class user_model(ndb.Model):
    username = ndb.StringProperty()

class ev_datastore(ndb.Model):
    vehicle_name = ndb.StringProperty()
    vehicle_manufacturer = ndb.StringProperty()
    vehicle_year = ndb.IntegerProperty()
    vehicle_battery_size = ndb.IntegerProperty()
    vehicle_WLTP_range = ndb.IntegerProperty()
    vehicle_cost = ndb.IntegerProperty()
    vehicle_power = ndb.IntegerProperty()
