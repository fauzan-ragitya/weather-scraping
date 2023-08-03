from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WeatherScraper(object):

    def __init__(self,
                 url="http://www.weather.gov.sg/climate-historical-daily/"):
        self.url=url
        driver = webdriver.Chrome()
        # driver.set_window_size(1920,1080)
        self.driver = driver
        driver.get(self.url)

    def get_element(self, by, value):
        if by=='id':
            result = self.driver.find_element(by=By.ID,value=value)
        elif by=='name':
            result = self.driver.find_element(by=By.NAME,value=value)
        elif by=='class':
            result = self.driver.find_element(by=By.CLASS_NAME,value=value)
        elif by=='text':
            xpath = f"//div[text()='{value}']"
            # xpath = f"//*[contains(text(), '{value}')]"
            result = self.driver.find_element(by=By.XPATH,value=xpath)
        return result
    
    def get_next_element(self, type,element):
        if type=='child':
            result = element.find_elements(By.XPATH,'*')
        elif type=='parent':
            result = element.find_elements(By.XPATH,'..')
        return result
    
    def change_text(self, element, new_text):
        script = f"arguments[0].innerText = '{new_text}'"
        self.driver.execute_script(script,element)

    def close_session(self):
        self.driver.quit()