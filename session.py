import time

from browserFactory import BrowserFactory
import genote
import notification
import setup


# Loading the settings dictionnary
settings = setup.load_configs()

# Simple script to monitor the website. If no difference is found in the HTML, the script waits
# for 10 minutes and sources the webpages again
initialGrades = None
updatedGrades = None
while True:
    
    driver = BrowserFactory.open_browser(settings['driver']) 
    genote.login(driver, settings['username'], settings['password'])
    updatedGrades = genote.source_classes_info(driver, settings['nbClasses'])
    driver.close()
    
    if initialGrades == None:
        initialGrades = updatedGrades
    
    else:
        if initialGrades != updatedGrades:
            notification.notify(initialGrades, updatedGrades)
            break

    time.sleep(600)
