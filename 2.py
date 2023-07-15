import numpy as np
import pandas as pd
import cv2 as cv
import matplotlib as mpl
import matplotlib.pyplot as plt
# from scipy.interpolate import griddata
# from scipy.interpolate import RBFInterpolator
from tqdm import tqdm
# import open3d as o3d
import os
from pyquaternion import Quaternion
img_file = './radiomap_f1.png'
img = cv.imread(img_file, cv.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray')
plt.show()