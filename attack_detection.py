from keras.models import load_model
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load the h5 model
attackDetectionModel = load_model('ai_models/cnn-lstm_attack_detection_model.h5')

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

class AttackDetection(Resource):
    def post(self):
        args =post_args.parse_args()

        # preprocess the email content 
        preprocessedFile = preprocessFile(args['file'])

        # Make predictions
        predictions = attackDetectionModel.predict(preprocessedFile)
        predictedClass =predictions.argmax(axis= 1)

        classes =['Dos Attack','Probe Attack','Privilege Attack','Access Attack','Normal']

        prediction_details = {
            'prediction': classes[predictedClass.item()],
            'prediction_accuracy': '{:.2f}%'.format(float(predictions[0][predictedClass.item()]) *100),
        }

        return {'data': prediction_details}
