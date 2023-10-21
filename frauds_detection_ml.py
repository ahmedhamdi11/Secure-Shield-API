from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler
import joblib


std_scaler = StandardScaler()
rob_scaler = RobustScaler()

# load the h5 model
fraudDetectionModel = joblib.load('ai_models/xgboost_model.pkl')

# argments
post_args = reqparse.RequestParser()
post_args.add_argument('file',
                        type =FileStorage,
                          help='file.csv is required',
                            required=True,
                            location ='files')


# preprocess the file 
def preprocessFile(file):
    df =pd.read_csv(file)

    rob_scaler = RobustScaler()

    df['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
    df['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))

    df.drop(['Time','Amount'], axis=1, inplace=True)

    scaled_amount = df['scaled_amount']
    scaled_time = df['scaled_time']

    df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
    df.insert(0, 'scaled_amount', scaled_amount)
    df.insert(1, 'scaled_time', scaled_time)
    return df

class FraudsDetectionMl(Resource):
    def post(self):
        args =post_args.parse_args()

        # preprocess the email content 
        preprocessedFile = preprocessFile(args['file'])

        # Make predictions
        pred = fraudDetectionModel.predict(preprocessedFile)

        predicted_label = "No Frauds" if pred[0] == 0 else "Frauds"
        
        prediction_details = {
            'prediction': predicted_label,
        }

        return {'data':prediction_details}
