from abc import ABC, abstractmethod
from seleniumwire import webdriver
import seleniumwire.undetected_chromedriver as uc


class Engine(ABC):
    def __init__(self) -> None:
        pass

class SeleniumEngine(Engine):
    def __init__(self, headless: bool, remote: bool = False, remote_ip_address: str = "") -> None:
        super().__init__()
        self.__headless = headless
        self.__remote = remote
        self.__remote_ip_address = remote_ip_address
        self.__driver = self.__get_selenium_driver()

    def __get_selenium_driver(self) -> webdriver.Chrome:
        if self.__remote:
            self.__driver = self.__start_remote_driver()
        else:
            self.__driver = self.__start_local_driver()
        return self.__driver

    def __get_driver_options(self) -> webdriver.ChromeOptions:
        """Get chrome driver options.
        """
        chrome_options = webdriver.ChromeOptions()
        if self.__headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--enable-javascript")
        return chrome_options

    def __start_local_driver(self) -> None:
        """This function creates a selenium driver and goes to this specified url.
        Once this is done, it waits self.waiting_time before returning the driver.
        """
        chrome_options = self.__get_driver_options()
        self.__driver = uc.Chrome(options=chrome_options)
    
    def __start_remote_driver(self) -> None:
        """Get remote selenium driver.
        """
        chrome_options = self.__get_driver_options()
        seleniumwire_options = {"address": self.__remote_ip_address}
        self.__driver = uc.Remote(command_executor = self.__remote_ip_address, options = chrome_options, seleniumwire_options = seleniumwire_options)

    def get_driver(self):
        return self.__driver

class AioHTTPEngine(Engine):
    def __init__(self) -> None:
        super().__init__()


# Engines should use retries and time strategies.
