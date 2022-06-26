#Want to know more about how the script works? Check out this video: https://youtu.be/rDBho83SUrw
#importing selenium and the necessary options options to login to FB 
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

#importing time libraries to add wait times 
from datetime import datetime
from time import sleep

#importing beautiful soup to read the page html source code  
from bs4 import BeautifulSoup

#to create csv file where we'll scrape the content
import pandas as pd


# we'll also add the options functionality to disable notifications
chrome_options = Options()
# disable notifications
chrome_options.add_argument("--disable-notifications")

# content_list=[]
# time_list=[]
name_list=[]
# comment_list=[]
# like_list=[]
# share_list=[]
link_list=[]
# cmttam_list=[]

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)

#accept cookies
# cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy"]'))).click()

email=driver.find_element_by_id("email")
email.send_keys("quoc.nguyen@tca.com.vn")
password=driver.find_element_by_id("pass")
password.send_keys("cESJJRs5K22wysD")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(2)
driver.get("https://www.facebook.com/groups/614192912041794/hashtags") # change group here
sleep(4)
time.sleep(2)
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i=0.5
while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")
    all_posts=soup.find_all("div",{"class":"rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw jifvfom9 gs1a9yip owycx6da btwxx1t3 cxgpxx05 b5q2rw42 lq239pai mysgfdmx hddg9phg"})
    for post in all_posts:
        try:
            name=post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v lrazzd5p oo9gr5id"}).get_text()
        except:
            name="name not found"
        print(name)
        # try:
        #     content=post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"}).get_text()
        # #except: to make sure that the code goes on even if there's nothing
        # except:
        #     content="content not found"
        # print(content)
        # try:
        #     time=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"}).get("aria-label")
        #     print(time)
        # except:
        #     time="time not found"

        try:
            link=""
            linkComplete="" 
            link=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 lrazzd5p"}).get("href")
            linkComplete="https://www.facebook.com"+link        
        except:
            link="link not found"    
        print(linkComplete) 
        

        # try:
        #     like=post.find("span",{"class":"pcp91wgn"}).get_text()
        #     # print(like)
        # except:
        #     like="like not found"
        # print(like)  

        # all_action=post.find_all("div",{"class":"oajrlxb2 gs1a9yip mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o tgvbjcpo hpfvmrgz esuyzwwr f1sip0of n00je7tq arfg74bv qs9ysxi8 k77z8yql pq6dq46d btwxx1t3 abiwlrkh lzcic4wl dwo3fsh8 g5ia77u1 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv gmql0nx0 kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h du4w35lb gpro0wi8"})
        # cmttam=""
        # comment=""
        # for action in all_action:
        #     try:
        #         comment=action.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain"}).get_text()
        #         cmttam=comment+","+cmttam           
        #     except:
        #         comment="comment not found"  
        # print(comment) 
        # print(cmttam)

        # content_list.append(content)
        # time_list.append(time)
        name_list.append(name)
        # comment_list.append(comment)
        # share_list.append(share)
        link_list.append(linkComplete)
        # like_list.append(like)
        # cmttam_list.append(cmttam)

        df=pd.DataFrame({"name":name_list,"link":link_list,})
        df.drop_duplicates(subset ="name",keep = "first", inplace = True)
        df.to_csv("facebookdata2.csv") #change the filename here

        if df.shape[0]>300: #by default, you'll get 10 posts, but if you want more or less, change the number here
            break
    if df.shape[0]>300:
        break
    # sleep(5)
    # y = 500
    # for timer in range(0, 25):
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 0.5
    #time.sleep(1)
    sleep(1)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 
        # y += 500
        # print(y)
        # sleep(2)

driver.quit() 