from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import bs4


def login(driver, userID, userPWD):
    """
    Entering user credentials to access genote.
    """
    actions = ActionChains(driver)
    driver.get('https://cas.usherbrooke.ca/login?service=https%3A%2F%2Fwww.usherbrooke.ca%2Fgenote%2Fpublic%2Findex.php')

    uidElem = driver.find_element_by_id('username')
    actions.send_keys_to_element(uidElem, userID)

    pwdElem = driver.find_element_by_id('password')
    actions.send_keys_to_element(pwdElem, userPWD)
    actions.send_keys(Keys.ENTER)
    actions.pause(2)
    actions.perform()

def source_classes_info(driver):
    
    # Getting the links on the website
    driver.get('https://www.usherbrooke.ca/genote/application/etudiant/cours.php')
    genoteSoup = bs4.BeautifulSoup(driver.page_source, features="html.parser")
    classesList = genoteSoup.find_all("a", href=True)

    # Filtering the links to keep only the classes links
    for cours in classesList[:]:
        
        if cours.text != 'Consulter':
            classesList.remove(cours)
    
    # Getting the status of every class on the site
    soups = []
    for link in classesList:
    
        driver.get('https://www.usherbrooke.ca/genote/application/etudiant/' + link['href'])
        soups.append(bs4.BeautifulSoup(driver.page_source, features="html.parser"))
        
    return soups

