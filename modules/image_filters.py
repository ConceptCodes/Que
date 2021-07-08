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

    # currently untested, this is from my wheres waldo project
    # will need major fracking the pixel version
    # will help if i finish up the part that gives you the region
    def _blur(self, region, gaussian=True, pixelated=False):
        if pixelated:
            (h, w) = region.shape[:2]
            xSteps = np.linspace(0, w, 21, dtype="int")
            ySteps = np.linspace(0, h, 21, dtype="int")
            for i in range(1, len(ySteps)):
                for j in range(1, len(xSteps)):
                    # compute the starting and ending (x, y)-coordinates
                    # for the current block
                    startX = xSteps[j - 1]
                    startY = ySteps[i - 1]
                    endX = xSteps[j]
                    endY = ySteps[i]
                    # extract the ROI using NumPy array slicing, compute the
                    # mean of the ROI, and then draw a rectangle with the
                    # mean RGB values over the ROI in the original region
                    roi = region[startY:endY, startX:endX]
                    (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
                    cv2.rectangle(region, (startX, startY), (endX, endY),
                        (B, G, R), -1)
            # return the pixelated blurred region
            return region
        else:
            h, w = region.shape[:2]
            kernel_width = (w // 7) | 1
            kernel_height = (h // 7) | 1

            face = cv2.GaussianBlur(face, (kernel_width, kernel_height), 0)
            img[start_y: end_y, start_x: end_x] = face

    def _background_audio(self, audio):
        pass