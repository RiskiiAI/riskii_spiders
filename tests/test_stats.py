import unittest
from riskii_spiders.core.stats import SpiderStats

class SpiderStatsTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.spider_stats = SpiderStats()

    def test_stats(self):
        pass
