#!/usr/bin/env python
import shutil
import argparse

from PIL import Image, ImageOps
import os
from os import path

parser = argparse.ArgumentParser("Image Rotator")
parser.add_argument('-c', '--clean', action="store_true")
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')
parser.add_argument('-s', "--step")

args = parser.parse_args()

origin_dir = args.input or "./images/"
result_dir = args.output or "./result_images/"

if args.clean:
    if path.exists(result_dir):
        shutil.rmtree(result_dir)

step = int(args.step) or 1

rotation_angles = range(0, 359, step)

img_names = os.listdir(origin_dir)

if not path.exists(result_dir):
    os.makedirs(result_dir)

for image_name in img_names:
    image_path = path.join(origin_dir, image_name)
    image = Image.open(image_path)
    for angle in rotation_angles:
        result_path = path.join(result_dir, f"{angle}_{image_name}")
        mirrored_result_path = path.join(result_dir, f"mirrored_{angle}_{image_name}")
        image.rotate(angle).save(result_path)
        ImageOps.mirror(image).rotate(angle).save(mirrored_result_path)
#
