from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
#from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import time
from selenium.common.exceptions import InvalidSelectorException
option = uc.ChromeOptions() 
option.headless = True
option.add_argument("--disable-notifications")

driver = uc.Chrome(options=option)
for numb in range(312,1,-1):
    try:
        
        page_err = driver.find_elements(by=By.XPATH, value='/html/body/div[1]/section/div[1]/h3/text()')
        driver.get(f'https://sextb.net/uncensored/pg-{numb}')
        
        print (('Đang Cào Page:'),numb)
                   
        links_data = driver.find_elements(by=By.XPATH, value='//*[@class="tray-item tray-item-uncensored"]/a')
        time.sleep(10)
           
                    
        links = [] 
        for i in links_data:
            if i == 0 :
                print ('Loi 0 Video')
                break
            else:
                links.append(i.get_attribute('href'))
                #next
        
        print ('Có',(len(links)),'Video')
        
        for x in links:
               driver.get(x)  
               title = driver.title
               print (title)
               server = driver.find_element(by=By.XPATH, value="//*[@class='btn-player episode']").click()
               wait = WebDriverWait(driver, 20*60)
               element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mol-vast-skip-control enabled']")))
               element.click()
               link = driver.find_element(by=By.XPATH, value="//div[@id='sextb-player']/iframe").get_attribute('src')
               if link is not None:
                    print('Link Ok')
                    result = link.split('?')
                    link_ok = (result[0])
                    print (link_ok)
                                                        
                    #API
                    #driver.get(f'https://doodapi.com/api/upload/url?key=152212ka9vejtprcxcvo88&url={link_ok}')
                    
                    nid_data = pd.DataFrame({'Title': [title],
                          'Link': [link_ok]})
                    nid_data['index_'] = np.arange(1, len(nid_data) + 1)
                         
                                    
                
               else:
                    print('Chua co link Dood')
                                           
    except InvalidSelectorException:
        print('Lỗi')
        break

driver.quit()    


                       