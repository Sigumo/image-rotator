#!/usr/bin/env python
import shutil

from PIL import Image, ImageOps
import os
import sys

args = sys.argv[1:]
origin_dir = "./images/"
result_dir = "./result_images/"

if "-c" in args or "--clean" in args:
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)

rotation_angles = [0, 90, 180, 270]

img_names = os.listdir(origin_dir)

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

for image_name in img_names:
    image = Image.open(origin_dir + image_name)
    for angle in [0, 180]:
        image.rotate(angle).save(result_dir + f"{angle}_{image_name}")
        ImageOps.mirror(image).rotate(angle).save(result_dir + f"mirrored_{angle}_{image_name}")
    image.transpose(Image.Transpose.ROTATE_90).save(result_dir + f"90_{image_name}")
    ImageOps.mirror(image).transpose(Image.Transpose.ROTATE_90).save(result_dir + f"mirrored_90_{image_name}")
    image.transpose(Image.Transpose.ROTATE_270).save(result_dir + f"270_{image_name}")
    ImageOps.mirror(image).transpose(Image.Transpose.ROTATE_270).save(result_dir + f"mirrored_270_{image_name}")

