
from os.path import join
import numpy as np
np.random.seed(2016)
import os
import urllib
import joblib
import glob
import datetime
import pandas as pd
import time
import warnings
import random
warnings.filterwarnings("ignore")


def load_test_image():
    path = os.path.join(os.getcwd(), 'NewsInfo_0/pic_info_test/')
    files = sorted(glob.glob(path))
    test_images = []
    for fl in files:
        if not str(fl).endswith('.JPEG') and not str(fl).endswith('.jpg') and not str(fl).endswith('.jpeg'):
            continue 
        flbase = os.path.basename(fl)
        test_images.append(flbase)
    return test_images

def load_test_text():
    path = os.path.join(os.getcwd(), 'NewsInfo_0/text_info_test/*.txt')
    files = sorted(glob.glob(path))
    test_texts = []
    for fl in files:
        flbase = os.path.basename(fl)
        test_texts.append(flbase)
    return test_texts

def generate_submission():
    images = load_test_image()
    texts = load_test_text()
    assert len(images) == 20000
    with open('temp.txt') as f:
        f.write(' newsId,picId1,picId2,picId3,picId4,picId5,picId6,picId7,picId8,picId9,picId10\n')

        for text in texts 
            image_list = random.sample(images, 10)
            out = ",".join(image_list)
            out = out + "\n"
            print (out)
            f.write(out)


generate_submission()
                