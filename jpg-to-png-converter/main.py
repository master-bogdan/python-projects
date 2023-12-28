import sys

from utils.path_normalizer import path_normalizer
from image_converter import image_converter

image_folder = path_normalizer(sys.argv[1])
output_folder = path_normalizer(sys.argv[2])

image_converter(image_folder, output_folder)
