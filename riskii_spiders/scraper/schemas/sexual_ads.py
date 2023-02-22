from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from riskii_spiders.scraper.scraper import RiskiiScraper
from typing import List

class SexualAdsScraper(RiskiiScraper):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_link(self) -> str:
        pass

    @abstractmethod
    def get_id(self) -> str:
         pass

    @abstractmethod
    def get_images_url(self) -> List[str]:
        pass

    @abstractmethod
    def get_is_verified(self) -> int: 
        pass

    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_phone(self) -> str:
        pass

    @abstractmethod
    def get_rates(self) -> dict:
        pass

    @abstractmethod
    def get_reviews(self):
        pass

    @abstractmethod
    def get_details(self) -> dict:
        pass

    @abstractmethod
    def get_website(self) -> str:
        pass

    @abstractmethod
    def get_city(self) -> str: 
        pass

    @abstractmethod
    def get_country(self) -> str: 
        pass

    @abstractmethod
    def get_statistics(self):
        pass

    @abstractmethod
    def get_is_prepayment(self):
        pass

    def extract_data(self, url: str) -> dict:
        data = {

        }
        return data