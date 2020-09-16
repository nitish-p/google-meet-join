from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time


def login(meetid):
    try:
        opt = webdriver.ChromeOptions()
        opt.add_argument( "--disable-infobars" )
        opt.add_argument( "start-maximized" )
        opt.add_argument( "--disable-extensions" )
        # block all sitesetting popup
        opt.add_experimental_option( "prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        } )
        driver = webdriver.Chrome( ChromeDriverManager().install(), options=opt )
        driver.get(r'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.210058069.1732524487.1599473504-670690007.1599473504&flowName=GlifWebSignIn&flowEntry=ServiceLogin' )
        driver.implicitly_wait( 15 )
        #ur gmail account must not have 2 step authentication and less secure is disabled in account setting
        gmailId = "Username" #enter username here

        passWord = "Password" #enter Password here
        
        time.sleep( 2 )
        loginBox = driver.find_element_by_xpath( '//*[@id ="identifierId"]' )
        loginBox.send_keys( gmailId )

        nextButton = driver.find_elements_by_xpath( '//*[@id ="identifierNext"]' )
        nextButton[0].click()
        time.sleep( 3 )
        passWordBox = driver.find_element_by_xpath( '//*[@id ="password"]/div[1]/div / div[1]/input' )
        passWordBox.send_keys( passWord )

        nextButton = driver.find_elements_by_xpath( '//*[@id ="passwordNext"]' )

        nextButton[0].click()
        time.sleep( 3 )
        driver.get( meetid )

        time.sleep( 3 )
        driver.find_element_by_xpath( '/html/body' ).click()
        time.sleep( 3 )

        ActionChains(driver).key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
        print( 'tried to join' )

        time.sleep( 2 )

        try:
            driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div').click()
        except:
            print('already joined')
            try:
                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
            except:
                print("failed")

        
        time.sleep(3600)
        print( 'alldone' )
    except:
        print( 'Login Failed' )


# meetid = r'https://meet.google.com/urr-ymbk-ytu' #put ur meet id here
# login( meetid )
