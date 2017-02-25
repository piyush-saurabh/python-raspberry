import RPi.GPIO as GPIO		# Import GPIO library
import time			# Import library to use 'sleep'

# Configure the GPIO to use the physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Configure the pin 7 to receive the output
GPIO.setup(7, GPIO.OUT)

# Function to blink the LED
def Blink(numberOfTimes, speed):
	try:
		for i in range(0, numberOfTimes):
			print "Number of blink(s) : " + str(i+1)
		
			# Turn the LED ON
			GPIO.output(7, True)
			# Sleep for 'speed' second
			time.sleep(speed)
	
			# Turn the LED OFF
			GPIO.output(7, False)
			time.sleep(speed)

		print "==========END==========" 
	
	except Exception,e:
		print "Error message : " + str(e)

	finally: 
		# Release all the GPIO pins
		GPIO.cleanup()

# Ask for inputs from the user
# numberOfTimes		: Number of times LED blinks
# speed			: Rate at which LED blinks
numberOfTimes = raw_input("Enter the number of times you want to blink the LED: ")
speed = raw_input("Enter the duration of each blink : ")

# Call the Blink() method
Blink(int(numberOfTimes), int(speed))

 
