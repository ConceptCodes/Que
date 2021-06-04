import cvlib as cv
from cvlib.object_detection import YOLO

class Susanoo():
    def __init__(self, video):
        self.frames = video

    def _detect_faces(self):
        tmp=[]
        for img in self.frames:
            tmp = faces, confidences = cv.detect_face(img, enable_gpu=True)
        return tmp

    def _detect_que_card(self):
        pass

    def _train_new_que_card(self, card):
        pass

    def _detect_objects(self, category='all'):
        tmp=[]
        yolo = YOLO('./yolo/yolov3.weights', './yolo/yolov3.cfg', './yolo/coco.names')
        for img in self.frames:
            bbox, label, conf = yolo.detect_objects(img)
            tmp.append((bbox, label, conf))
            #yolo.draw_bbox(img, bbox, label, conf)
        return tmp