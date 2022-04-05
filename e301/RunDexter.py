#!/usr/bin/env python3
import subprocess

while True:
    subprocess.call(['sh','./WakeWord.sh'])
    print ("Recording")
    subprocess.call(['sh','./RecordAudio.sh'])
    print ("Done")
    subprocess.call(['sh','./SpeechToText.sh'])
