__author__ = 'Jeff'
from PIL import Image
import os


iconImage =  "iTunesArtwork.png"
iconPath = 'iOS icons/Appstore/'
iconFileType = '.png'

def createIcons(iconImage, iconPath, iconFileType):

    print "Creating iOS icons..."
    print "Icons created in folder: Artwork"
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

    new_img = img.resize((80,80), Image.ANTIALIAS)
    new_img.save('%sIcon-80%s' % (iconPath, iconFileType))


createIcons(iconImage, iconPath, iconFileType)
