import os
from PIL import Image

from utils.path_normalizer import path_normalizer


def image_converter(image_folder, output_folder = ''):
    '''
      Function for converting from jpg to png format
    '''

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(image_folder):
        print(f'Processing image {filename}')
        img = Image.open(path_normalizer(f'{image_folder}/{filename}'))
        clean_name = os.path.splitext(filename)[0]
        img.save(path_normalizer(f'{output_folder}/{clean_name}.png'), 'png')
        print(f'Converted image {clean_name}.png')

    print('All images processed')
