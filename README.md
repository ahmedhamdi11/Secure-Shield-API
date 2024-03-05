
# Secure Shield API
Welcome to the Secure Shield API documentation. The Secure Shield API is a robust interface designed to empower applications with advanced cybersecurity features, including the detection of malware, phishing emails, frauds, and attack detection.
Additionally, it serves as a knowledge resource, offering articles on cybersecurity and user protection strategies. 


## API Endpoints Overview
The Secure Shield API comprises four main endpoints, each tailored to a specific aspect of cybersecurity:
- Attack Detection Endpoint
- Fraud Card Detection Endpoint
- Malware Detection Endpoint
- Phishing Email Detection Endpoint



## Below is a detailed description of each endpoint

### 1. Attack Detection Endpoint
- Description: Utilizes a Convolutional Neural Network (CNN) AI model to identify and classify network attacks.

- Model Output Classes: 'Dos Attack', 'Probe Attack', 'Privilege Attack', 'Access Attack', 'Normal'.

- Request Endpoint: POST /attack_detection

- Response:
{
    'data':{
        'prediction': "<Attack_Type>",
        'prediction_accuracy': "<float_range_0_to_100>",
    }
}


### 2. Fraud Card Detection Endpoint
- Description: Employs a Gated Recurrent Unit (GRU) model to detect fraudulent card activity and returns a prediction along with the model's confidence.

- Request Endpoint: POST /frauds_detection

- Response:
{
    'data':{
        'prediction': "<frauds_or_safe>",
        'prediction_accuracy': "<float_range_0_to_100>",
    }
}

### 3. Malware Detection Endpoint
- Description: Uses a Convolutional Neural Network (CNN) for the detection of malware in submitted files.

- Request Endpoint: POST /malware_detection

- Response:
{
    'data':{
        'prediction': "<safe_or_malware>",
        'prediction_accuracy': "<float_range_0_to_100>",
    }
}

### 4. Phishing Email Detection Endpoint
- Description: Utilizes a Gated Recurrent Unit (GRU) model to distinguish between phishing and safe emails.

- Request Endpoint: POST /phishing_email_detection

- Response:
{
    'data':{
        'prediction': "safe_or_phishing",
        'prediction_accuracy': "<float_range_0_to_100>",
    }
}



## Additional Resources Endpoint
Besides the primary security functionality, the Secure Shield API also provides an endpoint for accessing articles related to cybersecurity.

- Request Endpoint: GET /awareness

- Response:
{
  'data':
    [
      {
        'title':'<article_title>',
        'desc': '<full_article>',
        'image':'<related_article_image_url>',
      },
    ]

}


## Base URL
The API hase been hosted on Microsoft Azure.
And the base URL for accessing the Secure Shield API is: https://glory-team.azurewebsites.net

