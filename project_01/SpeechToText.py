# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
SpeechToText
--------------------------------------------------------------------------
License:   
Copyright 2021 Prithve Kiran Shekar
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
The brain behind Dexter. This program uses IBM Watson to transcrib the voice file, and send a command to the server using MQTT
Use your access keys in place of the placeholders below/
"""
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import paho.mqtt.client as mqtt
import paho.mqtt.publish
#Record Audio
# Record in chunks of 1024 samples
def everything():

    
    
    #Send to IBM
    #Using IBM's SDK to access their system.
    apikey = "<YOUR API KEY HERE>"
    url = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/fd8a23e8-4cd8-4001-82cf-5dde5bfa90bc"

    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open('testing.wav', 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/wav', model='en-US_NarrowbandModel').get_result()

    try:
        command = res['results'][0]['alternatives'][0]['transcript']
    except:
        command = 'room white' #In case nothing discernible from voice file
    print(command)


    #Send to Dexter
    client = mqtt.Client('dexhome')

    client.connect('<YOUR SERVER IP>')

    paho.mqtt.publish.single(
        topic='Room Control',
        payload=command,
        qos=2,
        hostname='<YOUR SERVER IP>',
        port=1883,
        auth={
            'username': '<YOUR MQTT USERNAME>',
            'password': '<YOUR MQTT PASSWORD'
            },
            )
    print('command sent')
    
everything()
