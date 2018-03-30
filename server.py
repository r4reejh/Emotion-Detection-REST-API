import falcon
import argparse
import sys, os
sys.path.append("../")
import cv2
import numpy as np
import face_detection_utilities as fdu
import VGG as vgg
FACE_SHAPE = (48, 48)
model = vgg.VGG_16('model_weights.h5')
emo     = ['Angry', 'Fear', 'Happy','Sad', 'Surprise', 'Neutral']


class WelcomeResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Face Detection API')



class DetectResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        emotion = self.getEmotion()
        resp.body = (emotion)
    def getEmotion(self):
        i=0
        capture = self.getCapture()
        seq = []
        while (i<5):
            flag, frame = capture.read()
            faceCoordinates = fdu.getFaceCoordinates(frame)
            if faceCoordinates is not None:
                face_img = fdu.preprocess(frame, faceCoordinates, face_shape=FACE_SHAPE)
                input_img = np.expand_dims(face_img, axis=0)
                input_img = np.expand_dims(input_img, axis=0)
                result = model.predict(input_img)[0]
                index = np.argmax(result)
                print (emo[index], 'prob:', max(result))
                seq.append(emo[index])
                i+=1
        return seq[2]
    def getCapture(self):
        capture = cv2.VideoCapture(0)
        if not capture:
            print("Failed to capture video streaming ")
            sys.exit(1)
        else:
            print("Succeded to capture video streaming")
        return capture


app = falcon.API()
welcome = WelcomeResource()
detect = DetectResource()
app.add_route('/', welcome)
app.add_route('/detect',detect)
    