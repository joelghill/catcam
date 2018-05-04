# import the necessary packages
import keras
from keras import layers
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications import inception_v3, resnet50
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")

args = vars(ap.parse_args())

#Load the ResNet50 model
#resnet_model = resnet50.ResNet50(weights='imagenet')

#Load the Inception_V3 model
inception_model = inception_v3.InceptionV3(weights='imagenet')

print("[INFO] Model loaded.")

# load the image
print("[INFO] loading the image")
original = load_img(args["image"], target_size=(224, 224))
print('PIL image size' + str(original.size))
 
# pre-process the image for classification
print("[INFO] preprocessing image...")
# convert the PIL image to a numpy array
# IN PIL - image is in (width, height, channel)
# In Numpy - image is in (height, width, channel)
numpy_image = img_to_array(original)
print('numpy array size',numpy_image.shape)
 
# Convert the image / images into batch format
# expand_dims will add an extra dimension to the data at a particular axis
# We want the input matrix to the network to be of the form (batchsize, height, width, channels)
# Thus we add the extra dimension to the axis 0.
image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)

# prepare image for resnet50 model
processed_image = inception_v3.preprocess_input(image_batch.copy())

# get the predicted probabilities for each class
predictions = inception_model.predict(processed_image)
# print predictions
 
# convert the probabilities to class labels
print(str(inception_v3.decode_predictions(predictions)))
