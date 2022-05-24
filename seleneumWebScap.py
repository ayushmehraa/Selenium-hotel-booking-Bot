import os
from selenium import webdriver
# for explict_waite function
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# our web driver is already in current folder(good peactice) so we can skip below step
os.environ['PATH']+=r"D:\GitHub Projects\web scrapping" 
#specifying location of webdriver, r is raw string **besure your driver version and browser verson is same(for example in our case edge and driver version is 98.0.1108.56)


driver=webdriver.Edge()
a=driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')#It will open edge and search of specified web address

#                      8 seconds
# driver.implicitly_wait(8)#specifying seconds to waite after opening web browser if element is not loaded(in case of slow web browser)if element is loaded then it will start an emidiate specified action.
# #after 3 seconds opening the web browser it will start the below action driver.implicitly_wait(30), no need to write it again and again for every action because it will execute itself before every action


myElement=driver.find_element_by_id('downloadButton')
myElement.click()

progressElement=driver.find_element_by_class_name('progress-label')
print(f"{progressElement.text}")

WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,'progress-lable'),  #Element filtration
        "Complete!" #Expected text
    )
)

