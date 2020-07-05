# Copyright 2020 Hiwot T. Sidelil, All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS"ssssssss9 BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import numpy as np
from skimage import io 
from skimage.transform import rotate, AffineTransform, warp
import random
from skimage import img_as_ubyte
import os
from pathlib import Path
from skimage.util import random_noise

def anticlockwise_rotation(image):
    angle= random.randint(0,180)
    return rotate(image, angle)

def clockwise_rotation(image):
    angle= random.randint(0,180)
    return rotate(image, -angle)

def gray_image(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def h_flip(image):
    return  np.fliplr(image)

def v_flip(image):
    return np.flipud(image)

def add_noise(image):
    return random_noise(image)

def blur_image(image):
    return cv2.GaussianBlur(image, (9,9),0)

def open_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def save_image(file_path, augmented_path, file_agum, image):
    (filename,ext) = os.path.splitext(file_path)
    new_image_path = augmented_path + Path(file_path).stem + file_agum + ext
    print("new path = ", new_image_path)
    transformed_image = img_as_ubyte(image)  #Convert an image to unsigned byte format, with values in [0, 255].
    transformed_image=cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB) #convert image to RGB before saving it
    cv2.imwrite(new_image_path, transformed_image) # save transformed image to path

images_path = "<folder path to all train and test/validation images>"
augmented_path = "<folder path where to store all augumented images>"
image_files=[] # to store paths of images from folder

for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array     
    image_files.append(os.path.join(images_path,im))
print("transforming images")

for image_file in image_files:
    save_image(image_file, augmented_path, "_agum_gray", gray_image(open_image(image_file)))
    save_image(image_file, augmented_path, "_agum_h_flip", h_flip(open_image(image_file)))  
    save_image(image_file, augmented_path, "_agum_noise", add_noise(open_image(image_file)))
    save_image(image_file,augmented_path, "_agum_blur", blur_image(open_image(image_file)))
