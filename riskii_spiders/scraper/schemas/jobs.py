
from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from riskii_spiders.scraper.scraper import RiskiiScraper

class JobsOffersScraper(RiskiiScraper):
    def __init__(self) -> None:
        super().__init__()

