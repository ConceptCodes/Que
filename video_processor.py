import cv2 as cv
import numpy as np

class Chidori(self):
    def __init__(self, input_path, output_path="test/output.mp4"):
        self.input_path= input_path 
        self.output_path= output_path
        self.vid_data= []

    def _load(self):
        cap = cv.VideoCapture(self.input_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            self.vid_data.append(frame)
            if cv.waitKey(1) == ord('q'):
                break
        print('{} loaded successfully!'.format(self.input_path))
        cap.release()

    def _render(self):     
        fourcc = cv.VideoWriter_fourcc(*'MJPG')
        out = cv.VideoWriter(self.output_path, fourcc, 20.0, (640,  480))
        for frame in self.vid_data:
            out.write(frame)
            if cv.waitKey(1) == ord('q'):
                break
        print('video saved to {}'.format(self.output_path))
        out.release()