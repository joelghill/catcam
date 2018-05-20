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

class CatVision :
    
    _model = None

    def __init__(self) :
        #Load the model
        self._model = inception_v3.InceptionV3(weights='imagenet')

    def identify_image(self, image_path) :
            
        # load the image
        print("[INFO] loading the image: " + image_path)
        original = load_img(image_path, target_size=(224, 224))
         
        # pre-process the image for classification
        print("[INFO] preprocessing image...")
        # convert the PIL image to a numpy array
        # IN PIL - image is in (width, height, channel)
        # In Numpy - image is in (height, width, channel)
        numpy_image = img_to_array(original)
         
        # Convert the image / images into batch format
        # expand_dims will add an extra dimension to the data at a particular axis
        # We want the input matrix to the network to be of the form (batchsize, height, width, channels)
        # Thus we add the extra dimension to the axis 0.
        image_batch = np.expand_dims(numpy_image, axis=0)

        # prepare image for resnet50 model
        processed_image = inception_v3.preprocess_input(image_batch.copy())

        # get the predicted probabilities for each class
        predictions = self._model.predict(processed_image)
        # print predictions
         
        # convert the probabilities to class labels
        decoded = resnet50.decode_predictions(predictions)
        friendly_predictions = CatVision._get_friendly_predictions(decoded[0])
        return friendly_predictions


    @staticmethod
    def _get_name(numpy_prediction) :
        name = numpy_prediction[1]
        name = name.replace('_', ' ')
        return name

    @staticmethod
    def _get_percentage(numpy_prediction) :
        return numpy_prediction[2] * 100

    @staticmethod
    def _get_friendly_predictions(numpy_predictions) :
        predictions = {}
        for prediction in numpy_predictions :
            name = CatVision._get_name(prediction)
            percentage = CatVision._get_percentage(prediction)
            predictions[name] = percentage

        return predictions
