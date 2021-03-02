from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class ChromeAutenticao:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver')
        


    def Trocar_Flow(self):
        self.driver.get('https://www.huggy.app/?return=https%3A%2F%2Flegacy.huggy.app%2Fpanel%2F')
        self.driver.maximize_window()
        print('tudo certo')


        time.sleep(2)
        camp_email = self.driver.find_element_by_xpath('//*[@id="input_11"]').click()
        camp_email.send_keys('luanportugal@gmail.com')

        #time.sleep(2)
        #button_google= self.driver.find_element_by_xpath('//*[@id="app"]/main/section/div/div/div/div/div/button[1]').click()

        #login = self.driver.find_element_by_xpath('//*[@id="app"]/main/section/div/div/div/div/div/button[2]')
        #login.click()
        #sleep(2)
        

bot = ChromeAutenticao()
bot.Trocar_Flow()
