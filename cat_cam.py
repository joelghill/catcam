from cam_tweet import CamTweets
from cat_vision import CatVision
from motion_sensor import MotionDetector
import os
import os.path
from picamera import PiCamera
from time import sleep
import argparse

class CatCam : 

    vision = None
    tweet = None
    motion = None
    camera = None

    images_directory = './Images'
    image_count = 0

    def initialize(self) :
        self.tweet = CamTweets()
        self.tweet.authorize()
        self.vision = CatVision()
        self.motion = MotionDetector(self.tweet_image)
        self.image_count = self.get_image_count()
        self.camera = PiCamera()
        self.camera.vflip = True

    def get_image_count(self) :
        return len(os.walk(self.images_directory).next()[2])

    def take_picture(self) :
        self.camera.start_preview()
        sleep(10)
        self.camera.capture(self.images_directory + "/" + str(self.image_count) + ".jpg")
        self.camera.stop_preview()
        self.image_count = self.image_count + 1

    def compose_tweet(self) : 
        image_path = self.images_directory + "/" + str(self.image_count - 1) + ".jpg"
        contents = self.vision.identify_image(image_path)
        first_guess_name = contents.keys()[0]
        first_guess_value = contents.values()[0]
        second_guess = contents.keys()[1]

        text = "I'm %2.2f%% confident this is a %s. Might be a %s" % (first_guess_value, first_guess_name, second_guess)
        print("Potential tweet: " + text)
        print("Gonna tweet it")
        self.tweet.update_timeline(text, image_path)
        sleep(180)

    def tweet_image(self) :
        print("Motion detected: ")
        self.take_picture()
        self.compose_tweet()

    def start(self, startup_tweet=None) :
        if startup_tweet != None :
            self.tweet.update_timeline(startup_tweet)
        self.motion.start(0.5)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--message", required=False, help="Startup message")

#args = vars(ap.parse_args())
cat_cam = CatCam()
cat_cam.initialize()
cat_cam.start()
