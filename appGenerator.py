__author__ = 'Jeff'
#!/usr/bin/env python
import os, shutil, time, glob
import zipfile
from PIL import Image
import numpy as np
import jira.client, requests
from jira import JIRA

"""
This automates nearly everything. It creates all the iOS icons,
                                  Changes the color of all the Android drawable images,
                                  Replaces the color of the Landing Images(if you want),
                                  Creates all the sizes of Landing Images,
                                  Zips all the necessary files,
                                  Creates all the standard Jira issues,
                                  Assigns the right people to each issue,
                                  Uploads the images to the prpoer Jira issues

1. Change the appName and all the RGB colors
2. Make sure all the images files are in this same folder with the proper names
3. Update the JIRA info - Login, password, App Key. YOU HAVE TO CREATE THE PROJECT IN JIRA FIRST.
"""

appName = ' ENTER THE APP NAME '

iconImage = "iTunesArtwork.png"
iconPath = 'Appstore/'
iconFileType = '.png'
androidIconsPath = 'AndroidIcons/'
androidIconsExt = 'png'

#New values for Android drawable-xxhdpi
ar2, gr2, ab2 = 100, 200, 200

# Enter the RGB values for each image (Do you want to change their colors? Change next line to 'yes')
doYouWantToChangeLandingColors = "no"
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
projectKey = "ENTER THE JIRA PROJECT KEY "
# If you change the login info here, you also have to change it in def uploadjiraAttach
options = {'server': 'https://pointburst.atlassian.net'}
#jira = JIRA(options, basic_auth=('YOUR LOGIN', 'YOUR PASSWORD'))
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
    issuesList = ["create google analytics ID",  # :'jeffreyrenken',
              "Add Google Analytics IDs", #: 'psrinivas',
                "color values (iOS)", #: 'psrinivas',
                "App authorization form (iOS and android)", #: 'mick.twomey',
                "Android - Twitter  app in the app's own backend cluster", #: 'sitakanta',
                "iOS - Twitter app in the app's own backend cluster", #: 'psrinivas',
                "Android - FB app in the app's own backend cluster", #: 'sitakanta',
                "iOS - FB app in the app's own backend cluster", #: 'psrinivas',
                "Android - New landing page", #: 'sitakanta',
                "iOS -New Landing page", #: 'psrinivas',
                "Android - Email sign up required for registartion", #: 'sitakanta',
                "iOS - Email sign up required for registration", #: 'psrinivas',
                "Android - FB compliance included", #: 'sitakanta',
                "iOS- FB compliance included", #: 'psrinivas',
                "Android- Integration with Kaltura", #: 'sitakanta',
                "iOS-Integration of Kaltura", #: 'psrinivas',
                "Upload publisher credentials", #: 'mick.twomey',
                "Upload iOS artwork", #: 'rogerrohatgi',
                "Create P12 files", #: 'psrinivas',
                "Android - Updates files on SVN for Apstrata and commit", #: 'yogi',
                "create google playstore images", #: 'sitakanta',
                "Create Apple App Store images", #: 'psrinivas',
                "Upload android artwork", #: 'rogerrohatgi',
                "Android - GP - Link Sender ID", #: 'sitakanta',
                "Android - Add GCM to APIs and Auth in GDC", #: 'sitakanta',
                "Android - Create project in Google Developer Console", #: 'sitakanta',
                "iOS - Create certificates", #: 'psrinivas',
                "iOS - Create Facebook suffix" #: 'mick.twomey',
                ]


    assigneeList = ['jeffreyrenken',
                'psrinivas',
                'psrinivas',
                'mick.twomey',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'mick.twomey',
                'rogerrohatgi',
                'psrinivas',
                'yogi',
                'sitakanta',
                'psrinivas',
                'rogerrohatgi',
                'sitakanta',
                'sitakanta',
                'sitakanta',
                'psrinivas',
                'mick.twomey']



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
    url = ('https://pointburst.atlassian.net/rest/api/2/issue/%s/attachments' % issue)
    headers = {"X-Atlassian-Token": "nocheck"}
    # please uncomment to attach external file
    files = {'file': open('%s' % attachment, 'rb')}
    # upload file to issue
    # [USERNAME], i.e.: admin
    # [PASSWORD], i.e.: admin
    r = requests.post(url, auth=(' YOUR LOGIN ', 'YOUR PASSWORD '), files=files, headers=headers)
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
    if doYouWantToChangeLandingColors == "yes":
        print "Changing landing image colors"
        replaceColor(r2IF, g2IF, b2IF, insiderFeedImage)
        replaceColor(r2ML, g2ML, b2ML, mediaLibraryImage)
        replaceColor(r2SB, g2SB, b2SB, socialBurstImage)
        replaceColor(r2SF, g2SF, b2SF, socialFeedImage)
    else:
        print "Landing image color NOT changed"

    createInsiderFeed()
    createMediaLibrary()
    createSocialBurst()
    createSocialFeed()
    zipf = zipfile.ZipFile('LandingArt.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('Artwork/', zipf)
    zipf.close()
    deleteDirectory('Artwork/')

    #createJiraIssues()
    print "Creating Jira Issues"
    # Attach iOS Artwork KEY-18
    print "Uploading Artwork to Jira"

# Add attachments to JIRA issues
    #uploadjiraAttach('%s-18' % projectKey, 'LandingArt.zip')
    #uploadjiraAttach('%s-18' % projectKey, 'ITunesIcons.zip')
    #uploadjiraAttach('%s-23' % projectKey, 'AndroidArt.zip')

# Delete the newly created art after uploading
    os.remove('LandingArt.zip')
    os.remove('ITunesIcons.zip')
    os.remove('AndroidArt.zip')
    print "Done"


