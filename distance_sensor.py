#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class SonicDistanceMonitor() :

    _pin_trigger = 4
    _pin_echo = 17
    _is_running = False

    on_distance_change = None

    def __init__(self, callback, trigger=7, echo=11) :
        """
        Initializes a new instance of the SonicDistance class
        tigger is the GPIO pin connected to the trigger sensor pin
        echo is the GPIO pin connected to the echo sensor pin
        """
        self._pin_trigger = trigger
        self._pin_echo = echo
        self.on_distance_change = callback

    def start(self, offset, wait=0.5) :
        """
        Begins monitoring for distance changes
        offset - The amount of change in distance before callback is activated
        wait - wait time in seconds before checking distance changes
        """
        delta_offset = offset
        last_distance = None

        self._prepare()
        self._is_running = True

        print('Monitoring distance')
        while(self._is_running == True):
            distance = self._get_distance()
            if(last_distance != None):
                change = abs(distance - last_distance)
                if(change >= delta_offset and self.on_distance_change != None):
                    self.on_distance_change(distance)

            last_distance = distance
            time.sleep(wait)

    def stop(self):
        """
        Stops monitoring for distance. Cleans up GPIO
        """
        self._is_running = false
        GPIO.cleanup()

    def _prepare(self):
        """
        Prepares this instance for using the GPIO board 
        to interact with HC-SR04 distance sensor
        """
        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self._pin_trigger, GPIO.OUT)
            GPIO.setup(self._pin_echo, GPIO.IN, pull_up_down = GPIO.PUD_UP)

            print "Waiting for sensor to settle"
            time.sleep(1)

            print("ready to calculate distance")

        except Exception as e: 
            print("prepare call failed: " + str(e))
            self.print_config()
            raise

    def _get_distance(self):
        """
        Calculates and returns distance in meters to the nearest object 
        in front of the sensor
        """
        try:
            GPIO.output(self._pin_trigger, GPIO.LOW)
            GPIO.output(self._pin_trigger, GPIO.HIGH)
            
            GPIO.wait_for_edge(self._pin_echo, GPIO.RISING)
            pulse_start_time = time.time()

            GPIO.wait_for_edge(self._pin_echo, GPIO.FALLING)
            pulse_end_time = time.time()

            pulse_duration = pulse_end_time - pulse_start_time

            #speed of sound is 343m/s
            distance = round(pulse_duration * 343, 2)
            return distance

        except Exception as e:
            print("Failed to get distance: " + str(e))
            self.print_config()
            raise

    def print_config(self):
        print("Trigger Pin: " + str(self._pin_trigger))
        print("Echo Pin: " + str(self._pin_echo))



def print_distance(distance):
    print("Distance is: " + str(distance) + "m")

#monitor = SonicDistanceMonitor(print_distance)
#monitor.start(0.2)

