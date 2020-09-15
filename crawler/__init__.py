import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumRequest(object):
    driver = None
    _options = [] #[ '--headless', '--no-sandbox', '--disable-gpu', '--disable-logging' ]
    
    def __init__(self, driver_path, options=None):
        assert os.path.isfile( driver_path ), 'Not Found, driver: {}'.format( driver_path )
                
        if options is not None:
            self._options += options
            
        self.driver_path=driver_path
        self.chrome_options = self._make_options( self._options )
            
        self.driver = webdriver.Chrome( executable_path=self.driver_path, chrome_options=self.chrome_options )
        
    def get( self, url, callback=None, **kwargs ):
        if callback is not None:
            self.callback = callback

        self.url = url
        self.driver.get( url )

        return self.callback( response=self.driver, **kwargs )
    
    def _make_options( self, options ):
        made = Options()
        for opt in set( options ):
            made.add_argument( opt )
        return made