from keras_preprocessing.sequence import pad_sequences
import pickle
from keras.models import load_model

from flask_restful import Resource, reqparse

# load the h5 model
gruPhishingEmailsModel = load_model('ai_models/gru_phishing_emails_model.h5')

# argments
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
        prediction_accuracy = '{:.2f}%'.format(float(pred_prob[0][0]) *100) if pred[0][0] == 1 else '{:.2f}%'.format(100- float(pred_prob[0][0]) *100)
        prediction_details = {
            'prediction': predicted_label,
            'prediction_accuracy': prediction_accuracy,
        }

        return {'data':prediction_details}
