import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

os.environ["PATH"]+=r"C:\Users\Ayush Mehra\Documents\c vs code\.vscode\python revision"
driver=webdriver.Edge()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(2)

try:
    popUpBTN=driver.find_element(By.ID,'at-cv-lightbox-close')
    popUpBTN.click()
except:
    print("no elemnt to click(pop dosent appear)")

sum1=driver.find_element_by_id('sum1')
sum2=driver.find_element_by_id('sum2')

sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD2)#==12
sum2.send_keys(12)

btn=driver.find_element_by_css_selector('button[onclick="return total()"]')
btn.click()


