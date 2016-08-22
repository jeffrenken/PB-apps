# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# This is a test app only. User/password aren't obfuscated
# Logs in to Pointburst as
# Sends a burst with the first image from Instagram to whichever group you specify
# Add login info, a message, and probably a test group
# Can be ran continuously by changing timesToRun - Add a +1 to burstName somewhere so you can differentiate between bursts


login = ""
password = ""
burstName = 1              # For a written name, use quotes: "This is the burst name."
burstMessage = ""
group = ""            # Be careful with this one. Group name has to be entered exactly, and leaving it blank will send a burst to all.
                           # It should work to enter only the first few letters, but I don't guarantee it.
postToTwitter = "yes"      # use "yes" or "no"
postToFacebook = "yes"
postToLinkedin = "yes"
timesToRun = 1             # This should be obvious.


class Burst(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://go.pointburst.com/index.php?displayLogin=yes"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_burst(self):
        timesRan = 1

        while timesRan <= timesToRun:
            driver = self.driver
            driver.get(self.base_url + "/index.php?displayLogin=yes")
            driver.find_element_by_id("dijit_form_ValidationTextBox_0").clear()
            driver.find_element_by_id("dijit_form_ValidationTextBox_0").send_keys(login)
            driver.find_element_by_id("dijit_form_ValidationTextBox_1").clear()
            driver.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys(password)
            driver.find_element_by_id("dijit_form_Button_1").click()
            print "Logged in " + str(timesRan)
            time.sleep(4)

            #driver.find_element_by_xpath("(//input[@value=''])[4]").click()
            driver.find_element_by_css_selector("#posts > table.content > tbody > tr > td.label > div.readOnly > div.listInnerLabel").click()
            time.sleep(4)

            driver.find_element_by_css_selector("div.listInnerLabel").click()
            time.sleep(4)

            driver.find_element_by_id("dijit_form_ValidationTextBox_1").clear()
            driver.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys(burstName)
            driver.find_element_by_id("srcMessage").clear()
            driver.find_element_by_id("srcMessage").send_keys(burstMessage)
            print "Typed name and message " + str(timesRan)

            driver.find_element_by_xpath("//form[@id='dijit_form_Form_0']/ul/li[3]/div[5]/span/span").click()
            #time.sleep(4)

            #driver.find_element_by_xpath("(//input[@value=''])[8]").click()
            time.sleep(10)

            driver.find_element_by_css_selector("#mycategories > table.content > tbody > tr > td.label > div.readOnly > div.listInnerLabel").click()
            time.sleep(3)

            driver.find_element_by_css_selector("#Instagram > table.content > tbody > tr > td.label > div > div.listInnerLabel").click()
            driver.find_element_by_link_text("Share").click()
            print "Added image " + str(timesRan)
            time.sleep(3)

    #Uncheck "Post to Social Media accounts"
            driver.find_element_by_id("dijit_form_CheckBox_1").click()
            driver.find_element_by_css_selector("div.mutliTag-arrow").click()

    #Post to group
            #driver.find_element_by_id("dijit_form_ComboBox_0_popup1").click()
            groupSelect = driver.find_element_by_xpath(("//*[@class='dijitReset dijitMenuItem'][contains(.,'%s')]") % group)
            groupSelect.click()
            time.sleep(2)

    #Check/Uncheck the Twitter box
            twitterBox = driver.find_element_by_id("dijit_form_CheckBox_6")
            if postToTwitter == "no":
                if twitterBox.is_selected():
                    twitterBox.click()

            if postToTwitter == "yes":
                 if twitterBox.is_selected():
                    continue
                 else:
                    twitterBox.click()

    #Check/Uncheck the Facebook box
            facebookBox = driver.find_element_by_id("dijit_form_CheckBox_7")
            if postToTwitter == "no":
                if facebookBox.is_selected():
                    facebookBox.click()

            if postToFacebook == "yes":
                 if facebookBox.is_selected():
                    continue
                 else:
                    facebookBox.click()

    #Check/Uncheck the LinkedIn box
            LinkedinBox = driver.find_element_by_id("dijit_form_CheckBox_8")
            if postToLinkedin == "no":
                if LinkedinBox.is_selected():
                    LinkedinBox.click()

            if postToLinkedin == "yes":
                 if LinkedinBox.is_selected():
                    continue
                 else:
                    LinkedinBox.click()

    #Click initial Send
            driver.find_element_by_id("dijit_form_Button_7_label").click()
            time.sleep(4)

    #Confirm Send - Uncomment these two lines, and comment out the cancel section to send a burst.
            #driver.find_element_by_xpath("//*[@class='dijitReset dijitInline dijitButtonText'][contains(.,'Send')]").click()
            #print "Burst shared " + str(timesRan)

    #Cancel Send
            driver.find_element_by_xpath("//*[@class='dijitReset dijitInline dijitButtonText'][contains(.,'Cancel')]").click()
            #driver.find_element_by_id("dijit_form_Button_13_label").click()
            print "Burst cancelled " + str(timesRan)


            time.sleep(5)
            driver.find_element_by_link_text("Logout").click()
            print "Logged out " + str(timesRan)

            time.sleep(5)
            print "Times ran: " + str(timesRan)
            timesRan = timesRan + 1
            time.sleep(5)



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()





