import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imread
import glob 
import pdb

def img2mp4(img_path,out_vid_path):

    img = imread(img_path)
    frameSize = (img.shape[0], img.shape[1])

    out = VideoWriter(out_vid_path,VideoWriter_fourcc(*'DIVX'), 60, frameSize)

    for i in range(10):
        img1 = img.copy()
        out.write(img1)
    out.release()