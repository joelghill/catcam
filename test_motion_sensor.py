from motion_sensor import MotionDetector
import argparse

def print_detection() :
    print("Motion detected")

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--time", required=True, help="The wait time between distance checks")

args = vars(ap.parse_args())

wait_time = args["time"]

print("Starting test")
print("Wait time: " + str(wait_time))

monitor = MotionDetector(print_detection)
monitor.start(float(wait_time))
