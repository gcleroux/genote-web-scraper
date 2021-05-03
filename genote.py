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

def source_classes_info(driver, nbClasses):
    
    # Getting the links on the website
    driver.get('https://www.usherbrooke.ca/genote/application/etudiant/cours.php')
    genoteSoup = bs4.BeautifulSoup(driver.page_source, features="html.parser")
    classesList = genoteSoup.find_all("a", href=True)

    # Filtering the links to keep only the classes links
    for cours in classesList[:]:
        
        if cours.text != 'Consulter':
            classesList.remove(cours)
    
    # Getting the status of every active classes on genote
    soups = []
    for link in classesList[:nbClasses]:
    
        driver.get('https://www.usherbrooke.ca/genote/application/etudiant/' + link['href'])
        soups.append(bs4.BeautifulSoup(driver.page_source, features="html.parser"))
    
    # Sourcing the grades of every tracked pages    
    grades = {}
    
    for soup in soups:
        page_content = soup.find_all("tbody")
        del page_content[0:2]
        
        try:
            grades[str(soup.title)[7:13]] = page_content[0].text
        except IndexError as e:
            continue
        
    return grades
