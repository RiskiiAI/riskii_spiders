from runstats import Statistics
from collections import Counter
from riskii_spiders.utils.errors import zero_on_division_error
 
class SpiderStats:
    def __init__(self) -> None:
        self.time_connect_stats = Statistics()
        self.time_total_stats = Statistics()

        self.n_success = 0  # number of successful results returned to the user
        self.n_fatal_errors = 0  # number of errors returned to the user, after all retries

        self.n_attempts = 0  # total amount of requests made to Riskii Spiders, including retries
        self.n_429 = 0  # number of 429 (throttling) responses
        self.n_errors = 0  # number of errors, including errors which were retried

        self.status_codes = Counter()
        self.exception_types = Counter()
        self.api_error_types = Counter()

    @zero_on_division_error
    def throttle_ratio(self):
        return self.n_429 / self.n_attempts
    
    @zero_on_division_error
    def error_ratio(self):
        return self.n_errors / self.n_attempts

    @zero_on_division_error
    def success_ratio(self):
        return self.n_success / self.n_processed

    @property
    def n_processed(self):
        """ Total number of processed URLs """
        return self.n_success + self.n_fatal_errors
