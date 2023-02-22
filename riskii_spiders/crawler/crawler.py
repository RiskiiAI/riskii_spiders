from abc import ABC, abstractmethod
from riskii_spiders.core.engine import Engine
from riskii_spiders.core.spider import RiskiiSpider
from riskii_spiders.utils.errors import WebsiteOutsideScope
from typing import List
import pandas as pd
import os

class RiskiiCrawler(RiskiiSpider):
    def __init__(self, name: str, engine: Engine, start_urls: List[str] = []):
        super().__init__(name, engine)
        self.__start_urls = start_urls

    def crawl(self, url: str):
        pass




