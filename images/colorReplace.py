import glob, os
from PIL import Image
import numpy as np

# Finds the most common color in an image and replaces it with the values entered below
# setup to use .png files but can change below, will change all files in this same directory
# Retains transparency


# ENTER THE NEW RGB VALUES HERE
r2, g2, b2 = 11,200,200
# Enter the file extension to change
extension = 'png'
# File path to save to, will create if doesn't exist yet
savePath = '/Users/Jeff/PycharmProjects/images/NewImages/'


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.convert('RGB').getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    most_frequent_pixel = str(most_frequent_pixel)
    most_frequent_pixel = ''.join(c for c in most_frequent_pixel if c not in '(){}<>')
    return most_frequent_pixel


if not os.path.exists(savePath):
    os.makedirs(savePath)


for path in glob.glob("*.%s" % extension):
    im = Image.open(path)
    data = np.array(im)
    print "The most frequent color is: " + most_frequent_colour(im)

    colorList = most_frequent_colour(im).strip().split(',')
    r1 = int(colorList[1].strip())
    g1 = int(colorList[2].strip())
    b1 = int(colorList[3].strip())


# UNCOMMENT THIS TO ENTER YOUR OWN RGB VALUES
    #r1, g1, b1 = 202, 156, 59 # Original values


    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)

    im.save('%s%s' % (savePath, path))
