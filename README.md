#Arduino
## Python y Arduino
Para usar arduino con python, seguir los siguientes pasos:
- Cargar prototype.pde (que esta en APIarduino) en el microcontrolador de tu Arduino
- Importar la libreria Arduino en tu script python (mirar ejemplo)

###Ejemplo
	from APIarduino.arduino import Arduino
	import time

	b = Arduino('/dev/ttyACM0') #ver en que puerto esta funcionando arduino
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


**Mayor información**
[Python Arduino Prototyping API V2](https://github.com/vascop/Python-Arduino-Proto-API-v2).

