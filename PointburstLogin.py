__author__ = 'Jeff'

# Logs into Pointburst backend, clicks Review Insider Feed, clicks Logout
# If this doesn't work, it sends an email and Slack message
# create a plist file for continuous running/monitoring


from selenium import webdriver
import time, smtplib

from slacker import Slacker

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from email.header    import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#### Pointburst Login info ####
login = ''
password = ''

def Email():

    sender = "YOUR GMAIL ADDRESS"
    recipients = ['SEND TO ADDRESSES', '', '']
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "%s isn't loading." % (login)

    body = "Username %s isn't loading on the Pointburst backend" % (login)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, "GMAIL PASSWORD")
    text = msg.as_string()
    server.sendmail(sender, recipients, msg.as_string())
    server.quit()


def writeStatus():
    if success == 1:
        with open("/Users/graphicdesigner-1/Google Drive/output.txt", "a") as text_file:
            text_file.write(login + " " + status + "\n")

    if success == 0:
        with open("/Users/graphicdesigner-1/Google Drive/output.txt", "a") as text_file:
            text_file.write(login + " " + status + "\n")


######## Firefox for viewable, PhantomJS for no browser ##############


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
#browser = webdriver.Firefox(firefox_profile=firefox_profile)

browser = webdriver.Firefox()
#browser = webdriver.PhantomJS()
loginPage = 'https://go.pointburst.com/index.php'
browser.get(loginPage)
#assert 'Yahoo' in browser.title

elem = browser.find_element_by_id('dijit_form_ValidationTextBox_0')  # Find the search box
elem.send_keys(login + Keys.RETURN)

pw = browser.find_element_by_id('dijit_form_ValidationTextBox_1')  # Find the search box
pw.send_keys(password + Keys.RETURN)

button = browser.find_element_by_id('dijit_form_Button_1')
button.click()

time.sleep(10)
#browser.implicitly_wait(300) #### 20 seems to work

success = 0
status = "Failed"
try:
    link = browser.find_element_by_link_text('Review Insider Feed')
    link.click()
    time.sleep(7)
    #browser.implicitly_wait(300)  #### 10 seems to work
    link = browser.find_element_by_link_text('Logout')
    link.click()
    success = 1
    status = "Success - " + time.ctime()
    writeStatus()
    print status
    time.sleep(7)
    browser.quit()
except NoSuchElementException:
    success = 0
    writeStatus()
    time.sleep(7)
    Email()
    slack = Slacker('YOUR SLACK KEY')
    slack.chat.post_message('SLACK HANDLE TO SEND TO','Login Failed',username='SLACK USERNAME')
    status = "Fail - " + time.ctime()
    browser.quit()
    print status

#browser.implicitly_wait(300)
#browser.close()



"""
try:
    page_loaded = wait.until_not(
    lambda browser: browser.current_url == loginPage)
except TimeoutException:
    print "Loading timeout expired"

# Assert that the URL is now the correct post-login page
self.assertEqual(browser.current_url,correct_page, msg = "Successful Login")
"""

