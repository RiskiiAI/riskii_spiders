from functools import wraps
from selenium.common.exceptions import NoSuchElementException

def handle_errors(func):
    @wraps(func)
    def handle_error(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoSuchElementException as error:
            return None
        except Exception as error:
            return "Error"
            #logger.error(f"Error in function {func.__name__} {str(error)}")
    return handle_error

def zero_on_division_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return 0
    return wrapper

class WebsiteOutsideScope(Exception):
    pass