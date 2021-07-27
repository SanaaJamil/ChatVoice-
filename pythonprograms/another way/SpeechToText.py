import base64
import pip
import json
import websocket 
import ibm_cloud_sdk_core
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
##variables creating 

apikey = 'nqCwSNpprXfZiF0uY8_HPkQjIIAOKtxUyX3MdjOGzwsu'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/0a02c3e8-d37d-41a8-bd8b-da8ea088a8c1'
# Setup Service

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

# Perform conversion
with open('output2.mp3', 'rb') as f: # rb = Read only mode.

    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
res #not in with open method 
text = res['results'][0]['alternatives'][0]['transcript']
text

confidence = res['results'][0]['alternatives'][0]['confidence']
confidence
with open('text.txt', 'w') as out: #write the text to be reading by texttospeech.py
    out.writelines(text)

# Perform conversion
with open('output2.mp3', 'rb') as f: #read only mode. 
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-AU_NarrowbandModel', continuous=True).get_result()
res