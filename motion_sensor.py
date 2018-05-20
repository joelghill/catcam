#!/usr/bin/python
import RPi.GPIO as GPIO
import time

class MotionDetector() :

    _input_pin = 11
    _is_running = False

    _on_motion_detected = None

    def __init__(self, callback, input_pin=11) :
        """
        Initializes a new instance of the SonicDistance class
        tigger is the GPIO pin connected to the trigger sensor pin
        echo is the GPIO pin connected to the echo sensor pin
        """
        self._input_pin = input_pin
        self._on_motion_detected = callback

    def start(self, wait=0.5) :
        """
        Begins monitoring for distance changes
        offset - The amount of change in distance before callback is activated
        wait - wait time in seconds before checking distance changes
        """

        self._prepare()
        self._is_running = True

        print('Detecting motion...')
        while self._is_running == True :
            GPIO.wait_for_edge(self._input_pin, GPIO.RISING)
            self._on_motion_detected()

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
            GPIO.setup(self._input_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

            print "Waiting for sensor to settle"
            time.sleep(5)

            print("ready to detect motion")

        except Exception as e: 
            print("prepare call failed: " + str(e))
            self.print_config()
            raise

    def print_config(self):
        print("Input Pin: " + str(self._input_pin))

#monitor = SonicDistanceMonitor(print_distance)
#monitor.start(0.2)

