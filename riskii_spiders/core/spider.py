import datetime 
from riskii_spiders.core.stats import SpiderStats
from riskii_spiders.core.engine import Engine
from riskii_spiders.utils.errors import WebsiteOutsideScope
from abc import ABC, abstractmethod
import os 
import riskii_spiders.core.contants as ct
import json 

class RiskiiSpider():

    def __init__(self, name: str, engine: Engine, remote: bool = True) -> None:
        self._name = name
        self._engine = engine
        self._stats = SpiderStats() # Protected attribute
        self.__folder_path = self.__get_folder_path()
        self.__initialize_spider()

    def __initialize_spider(self):
        self.__create_temp_folder()

    def get_extraction_date(self) -> str:
        today = str(datetime.datetime.today().date())
        return today

    #@abstractmethod
    def enter_website(self, url: str):
        pass

    def __get_folder_path(self):
        path = os.path.join(ct.DATA_FOLDER, self._name)
        return path
    
    def __create_temp_folder(self):
        os.mkdir(self.__folder_path)

    def _save_data(self, data: dict):
        with open(f"{self.__folder_path}/{ct.OUTPUT_FILE}", "a") as outfile:
            json.dump(data, outfile)
            outfile.write("\n")

    def _check_url_inside_scope(self, url: str):
        if self._name not in url:
            raise WebsiteOutsideScope("Website URL does not contain the website name specified in the crawler constructor parameters.")
