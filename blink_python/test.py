__author__ = 'wil_jm'

from APIarduino.arduino import Arduino
import time

b = Arduino('/dev/ttyACM0')
pin = 13

######### SETUP  #########
#declare output pins as a list/tuple
b.output([pin])
##########################

########## LOOP ##########
for x in range(5):
    b.setHigh(pin)
    time.sleep(1)
    print b.getState(pin)
    b.setLow(pin)
    print b.getState(pin)
    time.sleep(1)
    print x

b.close()
##########################