import glob, os
from PIL import Image
import numpy as np


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.convert('RGB').getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    #compare("Most Common", image, most_frequent_pixel[1])
    print colour
    return most_frequent_pixel

img = Image.open('image.png')
most_frequent_colour(img)