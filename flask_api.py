from phishing_email_detection import PhisingEmailDetection
from frauds_detection import FraudsDetection

from flask import Flask
from flask_restful import Api

app =Flask(__name__)
api =Api(app)


api.add_resource(PhisingEmailDetection,'/phising_email_detection')
api.add_resource(FraudsDetection,'/frauds_detection')

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')