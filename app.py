from phishing_email_detection import PhishingEmailDetection
from frauds_detection import FraudsDetection
from attack_detection import AttackDetection
from malware_detection import MalwareDetection
from attack_detection_ml import AttackDetectionML
from frauds_detection_ml import FraudsDetectionMl
from awareness import Awareness

from flask import Flask
from flask_restful import Api

app =Flask(__name__)
api =Api(app)

api.add_resource(FraudsDetection,'/frauds_detection')
api.add_resource(Awareness,'/awareness')
api.add_resource(AttackDetection,'/attack_detection')
api.add_resource(MalwareDetection,'/malware_detection')
api.add_resource(PhishingEmailDetection,'/phishing_email_detection')
api.add_resource(AttackDetectionML,'/attack_detection_ml')
api.add_resource(FraudsDetectionMl,'/frauds_detection_ml')


if __name__ =='__main__':
    app.run(debug=False,host='0.0.0.0')