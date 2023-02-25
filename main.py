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
parser.add_argument('--crop-size')
parser.add_argument('--without-mirror', action="store_true")

args = parser.parse_args()

origin_dir = args.input or "./images/"
result_dir = args.output or "./result_images/"
crop_size = int(args.crop_size) or 640

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
        rotated_image = image.rotate(angle)
        ImageOps.fit(rotated_image, (crop_size, crop_size)).save(result_path)
        if not args.without_mirror:
            mirrored_result_path = path.join(result_dir, f"mirrored_{angle}_{image_name}")
            rotated_mirrored_image = ImageOps.mirror(image).rotate(angle)
            ImageOps.fit(rotated_mirrored_image, (crop_size, crop_size)).save(mirrored_result_path)
#
