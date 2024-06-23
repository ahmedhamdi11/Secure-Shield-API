from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# load the h5 model
model = joblib.load('ai_models/knn_model.pkl')

# arguments
post_args = reqparse.RequestParser()
post_args.add_argument('file',
                        type =FileStorage,
                          help='file.csv is required',
                            required=True,
                            location ='files'
                            )


# preprocess the file 
def preprocessFile(file):
    data =pd.read_csv(file)
    
    le = LabelEncoder()
    data['protocol_type']=le.fit_transform(data['protocol_type'])
    data['service']=le.fit_transform(data['service'])
    data['flag']=le.fit_transform(data['flag'])

    return data




class AttackDetectionML(Resource):
    def post(self):
        args =post_args.parse_args()

        # preprocess the email content 
        preprocessedFile = preprocessFile(args['file'])

        # Make predictions
        predictions = model.predict(preprocessedFile)

        classes =['Dos Attack','Probe Attack','Privilege Attack','Access Attack','Normal']

        prediction_details = {
            'prediction': classes[predictions[0]],
        }

        return {'data': prediction_details}
