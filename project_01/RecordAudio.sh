#A script to record audio, activating the LED connected to GPIO58 to indicate when recording is active.

echo 1 > /sys/class/gpio/gpio58/value
arecord -D hw:0,0 -f s16_le testing.wav -d 3 -r44100
echo 0 > /sys/class/gpio/gpio58/value
