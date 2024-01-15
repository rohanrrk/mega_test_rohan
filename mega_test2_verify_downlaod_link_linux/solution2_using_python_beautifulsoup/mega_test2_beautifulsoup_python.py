from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
import requests,re
from colorama import Fore

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class verifylinks:

    def __init__(self):
        self.all_links = []
        self.re_pattern = "https://mega.nz/linux/repo/.*/.*"
        self.main_url = "https://mega.io/desktop"
        self.soup = ""
        self.result = ""
        self.all_downloadable_links = ""
  
    def get_source_html(self):
        '''Get website source html '''
        
        source_html = requests.get(self.main_url,verify=False)
        self.soup = BeautifulSoup(source_html.text, "html.parser")
     
    def get_all_links(self):
        '''Get all the links from the webpage '''

        for link in self.soup.find_all('a'):
            url = link.get('href')
            if url:
                self.result = self.result + "\n"+url
    
        self.all_downloadable_links = re.findall(self.re_pattern,self.result)
        
    def verify_download_links(self):
        ''' Verify download link works '''
        
        for link in self.all_downloadable_links:
            status_code = requests.head(link,verify=False)
            if status_code.status_code == 200:
                print(Fore.BLUE+link+Fore.YELLOW+" --> "+Fore.GREEN+str(status_code))
            else:
                print(Fore.BLUE+link+Fore.YELLOW+" --> "+Fore.RED+str(status_code))
             
if __name__ == "__main__":
    ''' Test Case steps to verify all linux os download links for x86 and x64 '''
    
    verifylinksobj = verifylinks()
    verifylinksobj.get_source_html()
    verifylinksobj.get_all_links()
    verifylinksobj.verify_download_links()
   
