
from keras.preprocessing.sequence import pad_sequences
import pickle
from keras.models import load_model

from flask import Flask
from flask_restful import Api, Resource, reqparse

app =Flask(__name__)
api =Api(app)


#################################################################
## phishing Email detection using the GRU model

gruPhishingEmailsModel = load_model('gru_phishing_emails_model.h5')

post_args = reqparse.RequestParser()
post_args.add_argument('email', type =str, help='email is required', required=True)

# preprocess the email 
def preprocessEmail(email):
    max_len = 150

    tokenizer_file = "tokenizer.pkl"
    with open(tokenizer_file, 'rb') as handle:
        tok = pickle.load(handle)

    email_sequences = tok.texts_to_sequences([email])
    email_sequences_matrix = pad_sequences(email_sequences,maxlen=max_len)

    return email_sequences_matrix

class PhisingEmailDetection(Resource):
    def post(self):
        args =post_args.parse_args()

        # preprocess the email content 
        preprocessedEmail = preprocessEmail(args['email'])

        # Make predictions
        pred_prob = gruPhishingEmailsModel.predict(preprocessedEmail)
        pred = (pred_prob > 0.5).astype(int)  

        predicted_label = "Phishing Email" if pred[0][0] == 0 else "Safe Email"

        prediction_details = {
            'prediction': predicted_label,
            'prediction_accuracy': '{:.2f}%'.format(float(pred_prob[0][0]) *100) ,
        }

        return {'data':prediction_details}


api.add_resource(PhisingEmailDetection,'/phising_email_detection')


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')