import cvlib as cv
from cvlib.object_detection import YOLO

class Susanoo():
    def __init__(self, video):
        self.frames = video
        self.scenes = {}
        self.yolo_weights = './ml/yolo/yolov3.weights'
        self.yolo_cfg = './ml/yolo/yolov3.cfg'
        self.yolo_labels = './ml/yolo/coco.names'

    def _detect_faces(self):
        tmp=[]
        for img in self.frames:
            tmp = faces, confidences = cv.detect_face(img, enable_gpu=True)
        return tmp

    def _detect_que_card(self):
        # the goal is to find que card's
        # timestamp there location
        # populate scene object -> {poptag: (start,stop) }
        pass


    def _detect_objects(self, category='all'):
        tmp=[]
        yolo = YOLO(self.yolo_weights_path, self.yolo_cfg, self.yolo_labels)
        for img in self.frames:
            bbox, label, conf = yolo.detect_objects(img)
            tmp.append((label, bbox))
        return tmp