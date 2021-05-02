import json
from browserFactory import BrowserFactory
from notificationFactory import NotificationFactory
import genote
import time
from sys import platform


filename = 'settings.json'
driver = None

try:
    with open(filename) as f_obj:
        settings = json.load(f_obj)
        
except FileNotFoundError:
    settings = {}
    settings['username'] = input("Username : ")
    settings['password'] = input("Password : ")
    settings['driver'] = input("""Enter your browser from the list : 
    -> Firefox
    -> Chrome
    -> Edge
    -> Opera
    -> Safari
    """
    )
    settings['OS'] = platform

    with open(filename, 'w') as f_obj:
        json.dump(settings, f_obj)

# Simple script to monitor the website. If no difference is found in the HTML, the script waits
# for 10 minutes and sources the webpages again
grades = {}
prev = None

while True:
    driver = BrowserFactory.open_browser(driver, settings['driver']) 
    genote.login(driver, settings['username'], settings['password'])
    classesInfo = genote.source_classes_info(driver)

    for class_ in classesInfo:
    
        page_content = class_.find_all("tbody")
        del page_content[0:2]
        
        try:
            grades[str(class_.title)[7:13]] = page_content[0].text
        except IndexError as e:
            continue
        
    if prev == None:
        prev = grades
        driver.close()
        time.sleep(600)
    
    else:
        if prev != grades:
            driver.close()
            
            # There's an update on the site, sending notification
            for key in grades.keys():
                
                if prev[key] != grades[key]:
                    NotificationFactory.create_notification(settings['OS'], "New grade in " + key, "Good luck!")
                    
            break
        
        else:
            driver.close()
            time.sleep(600)
