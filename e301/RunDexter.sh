#Making sure that the LED connected to GPIO58 can be turned on
#Activating the usr3 LED to show that the program is active
#Running the Dexter voice assistant

echo "out" > /sys/class/gpio/gpio58/direction
echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness
python3 RunDexter.py
