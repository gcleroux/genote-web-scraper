from selenium import webdriver

class BrowserFactory:
    """
    Factory to create the correct browser automation.
    """
    
    @staticmethod
    def open_browser(driver_type):
        """
        Uses the selenium API to create a browser instance.
        """
        
        if driver_type == "firefox":
            return webdriver.Firefox()

        elif driver_type == "chrome":
            return webdriver.Chrome()
        
        elif driver_type == "edge":
            return webdriver.Edge()
        
        elif driver_type == "opera":
            return webdriver.Opera()
        
        elif driver_type == "safari":
            return webdriver.Safari()