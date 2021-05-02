from selenium import webdriver


class BrowserFactory:
    """
    Factory to create the correct browser automation.
    """
    
    @staticmethod
    def open_browser(driver, driver_type):
        """
        Uses the selenium API to create a browser instance.
        """
        
        if driver_type == "Firefox":
            driver = webdriver.Firefox()
            return driver
        
        elif driver_type == "Chrome":
            driver = webdriver.Chrome()
            return driver
        
        elif driver_type == "Edge":
            driver = webdriver.Edge()
            return driver
        
        elif driver_type == "Opera":
            driver = webdriver.Opera()
            return driver
        
        elif driver_type == "Safari":
            driver = webdriver.Safari()
            return driver
        
if __name__ == '__main__':

    driver = BrowserFactory.open_browser(driver, driver_type)
