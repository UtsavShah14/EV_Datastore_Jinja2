import os
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

from models import user_model, ev_datastore

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'], autoescape=True)


class AddEV(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('add_ev.html')
        self.response.write(template.render())
    
    def post(self):
        button = self.request.get('button')
        if button == 'Add Vehicle':
            name = self.request.get('vehicle_name')
            manufacturer = self.request.get('vehicle_manufacturer')
            cost = int(self.request.get('vehicle_cost'))
            power = int(self.request.get('vehicle_power'))
            year = int(self.request.get('vehicle_year'))
            WLTP_range = int(self.request.get('vehicle_WLTP_range'))
            battery_size = int(self.request.get('vehicle_battery_size'))
            
            validate = ev_datastore.query().filter(
                ev_datastore.vehicle_name == name.lower(),
                ev_datastore.vehicle_manufacturer == manufacturer.lower(),
                ev_datastore.vehicle_year == year
                ).fetch(keys_only=True)
            
            if validate:
                status = 'Exists'
            else:
                status = 'Updated'
                new_vehicle = ev_datastore(
                    vehicle_name=name.lower(), 
                    vehicle_manufacturer=manufacturer.lower(),
                    vehicle_cost=cost,
                    vehicle_power=power,
                    vehicle_year=year,
                    vehicle_WLTP_range=WLTP_range,
                    vehicle_battery_size=battery_size)
                new_vehicle.put()

            template = JINJA_ENVIRONMENT.get_template('add_ev.html')
            self.response.write(template.render({'status':status}))
        else:
            self.redirect('/')
