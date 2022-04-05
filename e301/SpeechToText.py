
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import paho.mqtt.client as mqtt
import paho.mqtt.publish
#Record Audio
# Record in chunks of 1024 samples
def everything():

    
    
    #Send to IBM
    apikey = "jyExFZTrpq38LnClW2Qyq9FDXf9Sp1bGyV2DWKsg_Mia"
    url = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/fd8a23e8-4cd8-4001-82cf-5dde5bfa90bc"

    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open('testing.wav', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel').get_result()

    try:
        command = res['results'][0]['alternatives'][0]['transcript']
    except:
        command = 'room white'
    print(command)


    #Send to Dexter
    client = mqtt.Client('dexhome')

    client.connect('192.168.1.124')

    paho.mqtt.publish.single(
        topic='Room Control',
        payload=command,
        qos=2,
        hostname='192.168.1.124',
        port=1883,
        auth={
            'username': 'dexter',
            'password': 'onetwo'
            },
            )
    print('command sent')
    
everything()
