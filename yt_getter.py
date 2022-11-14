import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium_stealth import stealth
import time

print('pew')
# x = requests.get('https://2ch.hk/c/catalog.html')

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://2ch.hk/c/catalog.html"
driver.get(url)
time.sleep(5)
driver.quit()




# links = soup.find_all('a')
#
# currentrun_filepath = 'playlist1.m3u'
#
#
# def check_exists(link_to_check):
#     with open(currentrun_filepath, 'a+') as fp:
#         lines = fp.readlines()
#         for row in lines:
#             if row.find(link_to_check) != -1:
#                 return True
#         return False
#
#
# for link in links:
#     stuff_link = link['href']
#     if stuff_link.endswith(".jpg") or stuff_link.endswith(".png"):
#         if not check_exists(stuff_link):
#             print(stuff_link)
#             playlist_file = open(currentrun_filepath, 'a+')
#             fixed_stuff_link = "https:"+stuff_link
#             playlist_file.write(fixed_stuff_link+"\n")
#             playlist_file.close()
#
#             filename = stuff_link.split("/")[-1]
#             r = requests.get(fixed_stuff_link, stream=True)
#
#             if r.status_code == 200:
#                 # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#                 r.raw.decode_content = True
#                 # Open a local file with wb ( write binary ) permission.
#                 with open("downloads/"+filename, 'wb') as f:
#                     shutil.copyfileobj(r.raw, f)
#
#                 print('Image sucessfully Downloaded: ', filename)
#             else:
#                 print('Image Couldn\'t be retreived')




