__author__ = 'Jeff'
from PIL import Image
import os

insiderFeedImage = "InsiderFeed.png"
mediaLibraryImage = "MediaLibrary.png"
socialBurstImage = "Social-Bursts.png"
socialFeedImage = "SocialFeed.png"

appName = raw_input('Enter the app name (adds it to the created folder):')


def create320Width(image):
    imagePath = 'Artwork/Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Artwork/Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Artwork/Images/Landing Screen/%s Default/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    if 'Social-Bursts' in image:
        img = Image.open(image)
        img = img.resize((320,202), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((320,73), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))

def create640Width(image):
    imagePath = 'Artwork/Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Artwork/Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Artwork/Images/Landing Screen/%s Default-568h@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    if 'Social-Bursts' in image:
        img = Image.open(image)
        img = img.resize((640,479), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((640,172), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))

def create750Width(image):
    imagePath = 'Artwork/Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Artwork/Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Artwork/Images/Landing Screen/%s Default-667h@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    if 'Social-Bursts' in image:
        img = Image.open(image)
        img = img.resize((750,561), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((750,202), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))

def create1242Width(image):
    imagePath = 'Artwork/Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Artwork/Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Artwork/Images/Landing Screen/%s Default-736h@x3/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    if 'Social-Bursts' in image:
        img = Image.open(image)
        img = img.resize((1242,929), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((1242,334), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))

def create640WidthDefault(image):
    imagePath = 'Artwork/Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Artwork/Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Artwork/Images/Landing Screen/%s Default@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    if 'Social-Bursts' in image:
        img = Image.open(image)
        img = img.resize((640,404), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((640,145), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))

def createInsiderFeed():
    create320Width(insiderFeedImage)
    create640Width(insiderFeedImage)
    create750Width(insiderFeedImage)
    create1242Width(insiderFeedImage)
    create640WidthDefault(insiderFeedImage)

def createMediaLibrary():
    create320Width(mediaLibraryImage)
    create640Width(mediaLibraryImage)
    create750Width(mediaLibraryImage)
    create1242Width(mediaLibraryImage)
    create640WidthDefault(mediaLibraryImage)

def createSocialBurst():
    create320Width(socialBurstImage)
    create640Width(socialBurstImage)
    create750Width(socialBurstImage)
    create1242Width(socialBurstImage)
    create640WidthDefault(socialBurstImage)

def createSocialFeed():
    create320Width(socialFeedImage)
    create640Width(socialFeedImage)
    create750Width(socialFeedImage)
    create1242Width(socialFeedImage)
    create640WidthDefault(socialFeedImage)


createInsiderFeed()
createMediaLibrary()
createSocialBurst()
createSocialFeed()