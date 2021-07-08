import cv2
import numpy as np

class Amaterasu(self):
    def __init__(self, frames):
        self.frames = frames
        self.width = self.frames[0].shape[0]
        self.height = self.frames[0].shape[1]

    def _color_overlay(self, color=(0,0,255), intensity=0.8):
        tmp=[]
        col = np.full((self.width, self.height, 3), color, np.uint8)
        for img in self.frames:
            tmp.append(cv2.addWeighted(img, intensity, col, float(1 - intensity), 0))
        return tmp

    def _speed(self, amt=1.0):
        pass

    def _blur(self, region):
        #apply a gaussian blur to the region in frame,
        # should work for faces, license plates, etc
        pass

    def _background_audio(self, audio):
        pass