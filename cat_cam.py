from cam_tweet import CamTweets
from cat_vision import CatVision
from distance_sensor import SonicDistanceMonitor
import os
import os.path
from picamera import PiCamera
from time import sleep

class CatCam : 

    vision = None
    tweet = None
    distance = None
    camera = None

    images_directory = './Images'
    image_count = 0

    def initialize(self) :
        self.tweet = CamTweets()
        self.tweet.authorize()
        self.vision = CatVision()
        self.distance = SonicDistanceMonitor(self.tweet_image)
        self.image_count = self.get_image_count()
        self.camera = PiCamera()

    def get_image_count(self) :
        return len([name for name in os.listdir(self.images_directory) if os.path.isfile(name)])

    def take_picture(self) :
        self.camera.start_preview()
        sleep(5)
        self.camera.capture(self.images_directory + "/" + str(self.image_count) + ".jpg")
        self.camera.stop_preview()
        self.image_count = self.image_count + 1

    def compose_tweet(self) : 
        image_path = self.images_directory + "/" + str(self.image_count - 1) + ".jpg"
        contents = self.vision.identify_image(image_path)
        tweet = "I'm %2.2f%% this is a %s. Might be a %s" % (contents.values()[0], contents.keys()[0], contents.keys()[1])
        print(tweet)

    def tweet_image(self, distance) :
        self.take_picture()
        self.compose_tweet()

    def start(self) :
        self.distance.start(0.2)

cat_cam = CatCam()
cat_cam.initialize()
cat_cam.start()
