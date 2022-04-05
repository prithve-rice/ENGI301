echo "out" > /sys/class/gpio/gpio58/direction
echo 1 > /sys/class/leds/beaglebone:green:usr3/brightness
python3 RunDexter.py
