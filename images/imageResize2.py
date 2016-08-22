from PIL import Image
import os

# Creates icons and Home screen slices for iOS
# Currently sized for large Social burst images and the three other smaller images
# images have to be in the same directory as this file and have teh following EXACT names:

appName = raw_input('Enter the app name:')
iconImage =  "iTunesArtwork.png"
insiderFeedImage = "InsiderFeed.png"
mediaLibraryImage = "MediaLibrary.png"
socialBurstImage = "Social-Bursts.png"
socialFeedImage = "SocialFeed.png"

iconPath = 'Artwork/Appstore/'
iconFileType = '.png'

def createIcons(iconImage, iconPath, iconFileType):
    if not os.path.exists(iconPath):
        os.makedirs(iconPath)

    #SaveIcon Images
    img = Image.open(iconImage)
    new_img = img.resize((29,29), Image.ANTIALIAS)
    new_img.save('%sIcon-29%s' % (iconPath, iconFileType))

    new_img = img.resize((50,50), Image.ANTIALIAS)
    new_img.save('%sIcon-50%s' % (iconPath, iconFileType))

    new_img = img.resize((100,100), Image.ANTIALIAS)
    new_img.save('%sIcon-50@2x%s' % (iconPath, iconFileType))

    new_img = img.resize((57,57), Image.ANTIALIAS)
    new_img.save('%sIcon-57%s' % (iconPath, iconFileType))

    new_img = img.resize((58,58), Image.ANTIALIAS)
    new_img.save('%sIcon-58%s' % (iconPath, iconFileType))

    new_img = img.resize((120,120), Image.ANTIALIAS)
    new_img.save('%sIcon-60@2x%s' % (iconPath, iconFileType))

    new_img = img.resize((180,180), Image.ANTIALIAS)
    new_img.save('%sIcon-60@3x%s' % (iconPath, iconFileType))

    new_img = img.resize((72,72), Image.ANTIALIAS)
    new_img.save('%sIcon-72%s' % (iconPath, iconFileType))

    new_img = img.resize((114,114), Image.ANTIALIAS)
    new_img.save('%sIcon-72@2x%s' % (iconPath, iconFileType))

    new_img = img.resize((120,120), Image.ANTIALIAS)
    new_img.save('%sIcon-120%s' % (iconPath, iconFileType))

    new_img = img.resize((29,29), Image.ANTIALIAS)
    new_img.save('%sIcon-Small%s' % (iconPath, iconFileType))

    new_img = img.resize((114,114), Image.ANTIALIAS)
    new_img.save('%sIcon-Small@2x%s' % (iconPath, iconFileType))

    new_img = img.resize((87,87), Image.ANTIALIAS)
    new_img.save('%sIcon-Small@3x%s' % (iconPath, iconFileType))

    new_img = img.resize((53,53), Image.ANTIALIAS)
    new_img.save('%sIcon%s' % (iconPath, iconFileType))

    new_img = img.resize((114,114), Image.ANTIALIAS)
    new_img.save('%sIcon@2x%s' % (iconPath, iconFileType))

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
        img = img.resize((640,172), Image.ANTIALIAS)
        img.save('%s%s' % (appNameDefaultPath, image))
    else:
        img = Image.open(image)
        img = img.resize((640,479), Image.ANTIALIAS)
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

def create640Width(image):
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


createIcons(iconImage, iconPath, iconFileType)
create320Width(insiderFeedImage)
create320Width(mediaLibraryImage)
create320Width(socialBurstImage)
create320Width(socialFeedImage)

create640Width(insiderFeedImage)
create640Width(mediaLibraryImage)
create640Width(socialBurstImage)
create640Width(socialFeedImage)

create750Width(insiderFeedImage)
create750Width(mediaLibraryImage)
create750Width(socialBurstImage)
create750Width(socialFeedImage)

create1242Width(insiderFeedImage)
create1242Width(mediaLibraryImage)
create1242Width(socialBurstImage)
create1242Width(socialFeedImage)

create640Width(insiderFeedImage)
create640Width(mediaLibraryImage)
create640Width(socialBurstImage)
create640Width(socialFeedImage)



