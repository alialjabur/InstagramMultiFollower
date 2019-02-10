from selenium import webdriver
import time
import traceback

x = 50000
y= 1
browser = webdriver.Chrome('C:\Users\\Downloads/chromedriver')

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
#time to login**
time.sleep(20)

browser.get('https://www.instagram.com/anime_official_instagram/')

time.sleep(50)
for _ in range(x):
    followButton = '/html/body/div[2]/div/div/div[2]/ul/div/li[' + str(y) + ']/div/div[2]/button'
    followButton2 = '/html/body/div[2]/div/div/div[2]/ul/div/li[' + str(y) + ']/div/div[3]/button'

    try:
        browser.find_element_by_xpath(followButton2).click()
    except Exception as err:
        try:
            browser.find_element_by_xpath(followButton).click()
        except:
            pass
    print 'Followed a new Awesome Person!'
    time.sleep(1.5)
    y = y + 1;