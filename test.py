import sys
import cv2
import os
import numpy as np 
from detection.MTCNNDetecor import MTCNNDetecor
from detection.detector import Detector
from detection.p_detector import PDetector
from train.model import P_Net,R_Net,O_Net
import train.config as config


test_mode = config.test_mode
thresh = config.thresh
min_face_size = config.min_face_size
stride = config.stride
out_path = config.out_path
detectors = [None,None,None]

mtcnn_detector = MtCNNDetector(detectors=detectors, min_face_size=min_face_size,
                               stride=stride, threshold=thresh)

if config.input_mode == '1':
	path = config.test_dir
	for item in os.listdir(path):
		img_path = os.path.join(path,item)
		img = cv2.imread(img_path)
		boxes_c,landmarks=mtcnn_detector.detect(img)
		for i in range(boxes_c.shape[0]):
			cv2.rectangle(img,(corpbbox[0], corpbbox[1]),(corpbbox[2], corpbbox[3]), (255, 0, 0), 1)
	
		cv2.imshow('img',img)
	cv2.destroyAllWindows()	
