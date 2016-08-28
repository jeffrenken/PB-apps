__author__ = 'Jeff'

#!/usr/bin/env python
import os, shutil, time, glob
import zipfile
from PIL import Image
import numpy as np
import jira.client, requests
from jira import JIRA

appName = 'appName'
iconImage =  "iTunesArtwork.png"
iconPath = 'Appstore/'
iconFileType = '.png'
androidIconsPath = 'AndroidIcons/'
androidIconsExt = 'png'
r2, g2, b2 = 11,176,60
androidSavePath = '/Users/Jeff/Desktop/ColorReplacedImages/'

#New values for Android drawable-xxhdpi
ar2, gr2, ab2 = 100, 200, 200

# Enter the RGB values for each image
insiderFeedImage = "InsiderFeed.png"
r2IF, g2IF, b2IF = 3,200,33
mediaLibraryImage = "MediaLibrary.png"
r2ML, g2ML, b2ML = 133,3,200
socialBurstImage = "Social-Bursts.png"
r2SB, g2SB, b2SB = 3,200,3
socialFeedImage = "SocialFeed.png"
r2SF, g2SF, b2SF = 3,3,200



# Jira stuff
# Update the projectKey to what you just created on their site
projectKey = "TPO"
# If you change the login info here, you also have to change it in def uploadjiraAttach
options = {'server': 'https://   [YOUR JIRA SITE]    .atlassian.net'}
jira = JIRA(options, basic_auth=('[JIRA LOGIN}', '[JIRA PASSWORD]'))
issueType = "Story"



def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def deleteDirectory(filename):
    if os.path.exists(filename):
        shutil.rmtree(filename)

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

def createIOSIcons(iconImage, iconPath, iconFileType):
    print "Creating iOS icons"

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

def replaceColor(r2, g2, b2, image):
    im = Image.open(image)
    data = np.array(im)
    colorList = most_frequent_colour(im).strip().split(',')
    r1 = int(colorList[1].strip())
    g1 = int(colorList[2].strip())
    b1 = int(colorList[3].strip())

    red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    data[:,:,:3][mask] = [r2, g2, b2]

    im = Image.fromarray(data)
    #im.show()
    im.save(image)

def androidIcons(r2, g2, b2):
    for path in glob.glob("ANDROID_drawable-xxhdpi/*.%s" % androidIconsExt):
        im = Image.open(path)
        data = np.array(im)
        #print "The most frequent color is: " + most_frequent_colour(im)

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
        im.save(path)
    zipf = zipfile.ZipFile('AndroidArt.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('ANDROID_drawable-xxhdpi/', zipf)
    zipf.close()

def createJiraIssues():
    issuesList = ["create google analytics ID", "do something else", 'Today is Friday']  # :'jeffreyrenken',

    assigneeList = ['admin', 'admin', 'kenadams', ]

    issue_dict = {}
    i = 0
    for things in issuesList:
        summary = issuesList[i]
        assignee = assigneeList[i]
        issue_dict = {
                     'project': {'key': projectKey},
                      'summary': summary,
                      'description': '',
                      'issuetype': {'name': issueType},
                      'assignee': {'name': assignee},
                       }
        i = i+1
        jira.create_issue(fields=issue_dict)

def uploadjiraAttach(issue, attachment):
    url = ('https://JIRA SITE.atlassian.net/rest/api/2/issue/%s/attachments' % issue)
    headers = {"X-Atlassian-Token": "nocheck"}
    # please uncomment to attach external file
    files = {'file': open('%s' % attachment, 'rb')}
    # upload file to issue
    # [USERNAME], i.e.: admin
    # [PASSWORD], i.e.: admin
    r = requests.post(url, auth=('admin', '[JIRA PASSWORD'), files=files, headers=headers)
    #print(r.status_code)
    #print(r.text)


if __name__ == '__main__':

    androidIcons(ar2, gr2, ab2)
    print "Creating Android artwork"
    zipf = zipfile.ZipFile('AndroidArt.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('ANDROID_drawable-xxhdpi/', zipf)
    zipf.close()


    createIOSIcons(iconImage, iconPath, iconFileType)
    zipf = zipfile.ZipFile('ITunesIcons.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(iconPath, zipf)
    zipf.close()
    deleteDirectory(iconPath)


    print "Creating Landing screen images"
    replaceColor(r2IF, g2IF, b2IF, insiderFeedImage)
    replaceColor(r2ML, g2ML, b2ML, mediaLibraryImage)
    replaceColor(r2SB, g2SB, b2SB, socialBurstImage)
    replaceColor(r2SF, g2SF, b2SF, socialFeedImage)

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

    create640WidthDefault(insiderFeedImage)
    create640WidthDefault(mediaLibraryImage)
    create640WidthDefault(socialBurstImage)
    create640WidthDefault(socialFeedImage)
    zipf = zipfile.ZipFile('LandingArt.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('Artwork/', zipf)
    zipf.close()
    deleteDirectory('Artwork/')


    createJiraIssues()
    print "Creating Jira Issues"
    # Attach iOS Artwork KEY-18
    print "Uploading Artwork to Jira"

    uploadjiraAttach('%s-12' % projectKey, 'LandingArt.zip')
    uploadjiraAttach('%s-13' % projectKey, 'ITunesIcons.zip')
    uploadjiraAttach('%s-14' % projectKey, 'AndroidArt.zip')



    #os.remove('LandingArt.zip')
    os.remove('ITunesIcons.zip')
    os.remove('AndroidArt.zip')



"""
    #shutil.copy2('Python.zip', 'Python2.zip')
    filename = 'Python.zip'
    time.sleep(5)
    deleteFile(filename)
    """
