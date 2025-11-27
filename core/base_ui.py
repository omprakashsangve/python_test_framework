from selenium import webdriver
from configparser import ConfigParser
import os

class BaseUI:
    def setup_browser(self):
        # Load config
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'config', 'config.ini')
        config = ConfigParser()
        config.read(config_path)

        browser = config.get('ui', 'browser')
        url = config.get('ui', 'base_url')

        # Launch browser
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Unsupported browser")

        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def teardown_browser(self):
        self.driver.quit()
