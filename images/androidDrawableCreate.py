import glob, os, zipfile
from PIL import Image
import numpy as np

# Finds the most common color in an image and replaces it with the values entered below
# setup to use .png files but can change below, will change all files in ANDROID_drawable-xxhdpi/
# Can also enter a specific RGB value below to change, but shouldn't have to for this purpose
# Retains transparency
# AndroidArt.zip will be in the same location as this file

# ENTER THE NEW RGB VALUES HERE
r2, g2, b2 = 44,78,35


# Enter the file extension to change
extension = 'png'
# File path to save to, will create if doesn't exist yet
#savePath = '/Users/Jeff/Desktop/ColorReplacedImages/'


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

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

#if not os.path.exists(savePath):
#    os.makedirs(savePath)


for path in glob.glob("ANDROID_drawable-xxhdpi/*.%s" % extension):
    im = Image.open(path)
    data = np.array(im)
    print "The most frequent color is: " + most_frequent_colour(im)

    colorList = most_frequent_colour(im).strip().split(',')
    r1 = int(colorList[1].strip())
    g1 = int(colorList[2].strip())
    b1 = int(colorList[3].strip())


# UNCOMMENT THIS TO ENTER YOUR OWN ORIGINAL RGB VALUES
    #r1, g1, b1 = 202, 156, 59 # Original values


    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)
    im.save(path)
    zipf = zipfile.ZipFile('AndroidArt.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('ANDROID_drawable-xxhdpi/', zipf)
    zipf.close()
print "AndroidArt.zip was created in " + os.getcwd()
