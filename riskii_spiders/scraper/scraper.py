from riskii_spiders.core.spider import RiskiiSpider
from riskii_spiders.core.engine import Engine
from typing import List
from abc import ABC, abstractmethod

class RiskiiScraper(RiskiiSpider):
    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self.__engine = engine

    @abstractmethod
    def extract_data(self, url: str) -> dict:
        pass

    @abstractmethod
    def test_scraper(self, url: str):
        pass