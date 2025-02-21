import requests  
import json

def emotion_detector(text_to_analyse):  
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobjt= { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = URL, json = myobjt, headers = Headers)  
    return response.text  # Return the response text from the API