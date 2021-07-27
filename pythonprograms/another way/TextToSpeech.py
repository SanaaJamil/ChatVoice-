#insatall all needed packages
#pip3 install ibm_watson


#import all needed packages

import base64
import pip
import json
import websocket 
import ibm_cloud_sdk_core
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


#create variables
apikey ='D7i84fmED0sA-gmabFh0JWoyOP6XmFb_BOT_wGSEYXl-'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/56137b4c-f7ae-47bf-bde8-e16669fdff9b'
# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)
#convert from text -welcoming text-
with open('./speech.mp3', 'wb') as audio_file: #Write only mode. #to welcome the customer
    res = tts.synthesize('welcome customer, please enter your massege', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
#read file -convert from .txt file-  
##### insert users input into this file to read it by robot #######
with open('text.txt', 'r') as f: 

    text1 = f.readlines()
    text1 = [line.replace('\n','') for line in text1]
    text1 = ''.join(str(line) for line in text1)
#####  read the content of text,txt by robot #######
with open('./speech2.mp3', 'wb') as audio_file:
    res = tts.synthesize(text1, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
