from flask import Flask
from flask_restful import Resource
class Awareness(Resource):
    def get(self):
        return {'data':[
         {
             "title": 'cyber security',
             "desc":'the practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks',
              "image": 'https://images.pexels.com/photos/6330644/pexels-photo-6330644.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1 ',
          },
         {
             "title": ' cyber security',
             "desc":'the practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks',
              "image": 'https://images.pexels.com/photos/5380642/pexels-photo-5380642.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1 ',
          },
       ]}