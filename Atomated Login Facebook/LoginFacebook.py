from selenium import webdriver 
from selenium.webdriver.common.by import By   

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome import service

#from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

import time 

url = 'https://www.facebook.com/login.php'
PAS = '0123456789lol@0123456789lol@'
EM  = ' '
BRW = 'Edge'

class FacebookLogin():
      def __init__(self,email,password,browser):
          
          self.email = email 
          self.password = password
          
          if browser == 'Opera':
            webdriver_service = service.Service(OperaDriverManager().install())
            webdriver_service.start()
            options = webdriver.ChromeOptions()
            options.add_experimental_option('w3c', True)
            self.driver  = webdriver.Remote(webdriver_service.service_url, options=options)
			 
          elif browser == 'Edge':
            self.driver  = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  

          self.driver.get(url)
          time.sleep(1) #1 sec 
          
      def login(self):
          email_element = self.driver.find_element(By.ID , 'email' )
          email_element.send_keys(self.email)

          password_element = self.driver.find_element(By.ID , 'pass' )
          password_element.send_keys(self.password)

          login_button = self.driver.find_element(By.ID , 'loginbutton' )
          login_button.click()

          time.sleep(20) #2 sec

if __name__ =='__main__' :
   fb_login = FacebookLogin(email=EM , password=PAS , browser=BRW)
   fb_login.login()