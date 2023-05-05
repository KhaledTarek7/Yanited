import RPi.GPIO as GPIO
import time


# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set up pins
PIR_sensor1 =11 
PIR_sensor2 = 13
m11 = 15
m12 = 29
buttonPin =36 



# Configure GPIO pins
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)

GPIO.setup(PIR_sensor1, GPIO.IN)
GPIO.setup(PIR_sensor2, GPIO.IN)
GPIO.setup(buttonPin, GPIO.IN)


def setup():
    
    time.sleep(3)
    
    time.sleep(2)
    

def loop():
    while True:
        if GPIO.input(PIR_sensor1) or GPIO.input(buttonPin):
            
            GPIO.output(m11, GPIO.HIGH)
            GPIO.output(m12, GPIO.LOW)
           
            
            time.sleep(10)
            

            
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)
           
            time.sleep(5)
            

        if GPIO.input(PIR_sensor2):
            
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.HIGH)
            
            time.sleep(10)
            

            
            GPIO.output(m11, GPIO.LOW)
            GPIO.output(m12, GPIO.LOW)
            

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        
