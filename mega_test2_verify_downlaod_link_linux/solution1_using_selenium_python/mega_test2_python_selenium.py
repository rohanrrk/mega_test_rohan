from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import requests,time
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore

class mainselenium:

    def __init__(self):
        self.all_linux_os = []
        
    def open_web_page(self):
        '''Initialize selenium webdriver and open the website'''
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://mega.io/desktop")
     
    def accept_cookies(self):
        '''Click accept the cookies button'''
        
        try:
            accept_cookie_button = self.driver.find_element(By.XPATH,"//button[contains(text(),'Accept all cookies')]")
            if accept_cookie_button.is_displayed():
                accept_cookie_button.click()
        except Exception ('ElementNotVisibleException'):
            print("Cookie accept pop up box not visible")
           
    def scroll_into_download_view(self):
        '''Scroll into the view of download div'''
        
        scroll_view = self.driver.find_element(By.XPATH, "//div[@class='scrollpoint']")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_view)
        
    def  click_on_linux_tab(self):
        '''Click on Linux Tab'''

        time.sleep(10)
        linux_tab = self.driver.find_element(By.XPATH, "//div[@class='linux tab']")
        linux_tab.click()
        
    def enumerate_all_linux_flavor(self):
        '''Get all Linux OS name'''
        
        linux_flavors = self.driver.find_elements(By.XPATH, "//span[@class='name']")
        for linux_flavor in linux_flavors:
            os_name = linux_flavor.get_attribute("innerText")
            self.all_linux_os.append(os_name)

    def enumerate_links_and_verify(self):
        '''Get all corresponding linux name download link'''
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        dropdown_list = self.driver.find_element(By.XPATH, "//div[@class='dropdown lg']")

        os_name = self.all_linux_os
        for os in range(1,len(self.all_linux_os)+1):

            dropdown_list.click()
            xpath_select_os = "(//div[@class='options-list']//span[@class='name'])["+str(os)+"]"
            
            os_select = self.driver.find_element(By.XPATH, xpath_select_os)
            self.driver.execute_script("arguments[0].scrollIntoView();", os_select)
            time.sleep(5)
            os_select.click()
            time.sleep(2)
  
            xpath_href_value = "//div[@class='product-card "+os_name[os-1].lower().replace(" ","-")+" desktop']/div[2]//div/child::a"
            xpath_get_links = self.driver.find_elements(By.XPATH, xpath_href_value)
            print(Fore.WHITE+"------ Verifying download links for OS "+os_name[os-1]+"------")
            for link in range(len(xpath_get_links)):
                url = xpath_get_links[link].get_attribute("href")
                status_code = requests.head(url,verify=False)
                if status_code.status_code == 200:
                    print(Fore.BLUE+url+Fore.YELLOW+" --> "+Fore.GREEN+str(status_code))
                else:
                    print(Fore.BLUE+url+Fore.YELLOW+" --> "+Fore.RED+str(status_code))

            self.driver.execute_script("arguments[0].scrollIntoView();", dropdown_list)
            time.sleep(5)            

if __name__ == "__main__":
    ''' Test Case steps to verify all linux os download links for x86 and x64 '''
    
    mainseleniumobj = mainselenium()
    mainseleniumobj.open_web_page()
    mainseleniumobj.accept_cookies()
    mainseleniumobj.scroll_into_download_view()
    mainseleniumobj.click_on_linux_tab()
    mainseleniumobj.enumerate_all_linux_flavor()
    mainseleniumobj.enumerate_links_and_verify()

# Test case using python and selenium
