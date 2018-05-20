from cat_vision import CatVision
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")

args = vars(ap.parse_args())

cat_vision = CatVision()
predictions = cat_vision.identify_image(args["image"])

for key in predictions :
   print(str(key) + " : " + str(predictions[key])) 

