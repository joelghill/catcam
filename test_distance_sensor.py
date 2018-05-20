from distance_sensor import SonicDistanceMonitor
import argparse

def print_distance(distance) :
    print("Distance change detected. Distance is now %1.2fm" % distance)

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--offset", required=True, help="The distance offset")
ap.add_argument("-t", "--time", required=True, help="The wait time between distance checks")

args = vars(ap.parse_args())

offset = args["offset"]
wait_time = args["time"]

print("Starting test")
print("Distance offset: " + str(offset))
print("Wait time: " + str(wait_time))

monitor = SonicDistanceMonitor(print_distance)
monitor.start(float(offset), float(wait_time))
