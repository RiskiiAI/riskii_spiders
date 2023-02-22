from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from riskii_spiders.scraper.scraper import RiskiiScraper

class PhoneNumbersScraper(RiskiiScraper):
    def __init__(self) -> None:
        super().__init__()