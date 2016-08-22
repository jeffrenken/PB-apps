from PIL import Image
import os

"""
imageFile = "screenImage.png"
im1 = Image.open(imageFile)
# adjust width and height to your needs
width = 500
height = 420
# use one of these filter options to resize the image
im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
ext = ".jpg"
im2.save("NEAREST" + ext)
im3.save("BILINEAR" + ext)
im4.save("BICUBIC" + ext)
im5.save("ANTIALIAS" + ext)
"""

appName = 'Ora'
iconImage =  "iTunesArtwork.png"
insiderFeedImage = "InsiderFeed.png"
mediaLibraryImage = "MediaLibrary.png"
socialBurstImage = "Social-Bursts.png"
socialFeedImage = "SocialFeed.png"

iconPath = 'Appstore/'
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
    imagePath = 'Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Images/Landing Screen/%s Default/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    basewidth = 320
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize= int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('%s%s' % (appNameDefaultPath, image))

def create640Width(image):
    imagePath = 'Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Images/Landing Screen/%s Ora Default-568h@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    basewidth = 640
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize= int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('%s%s' % (appNameDefaultPath, image))

def create750Width(image):
    imagePath = 'Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Images/Landing Screen/%s Ora Default-667h@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    basewidth = 750
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize= int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('%s%s' % (appNameDefaultPath, image))

def create1242Width(image):
    imagePath = 'Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Images/Landing Screen/%s Ora Default-736h@x3/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    basewidth = 1242
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize= int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('%s%s' % (appNameDefaultPath, image))

def create640Width(image):
    imagePath = 'Images/'
    if not os.path.exists(imagePath):
        os.makedirs(imagePath)

    landingScreenPath = 'Images/Landing Screen'
    if not os.path.exists(landingScreenPath):
        os.makedirs(landingScreenPath)

    appNameDefaultPath = ('Images/Landing Screen/%s Ora Default@x2/' % appName)
    if not os.path.exists(appNameDefaultPath):
        os.makedirs(appNameDefaultPath)

    basewidth = 640
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize= int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
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



