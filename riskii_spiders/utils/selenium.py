from riskii_spiders.utils.errors import handle_errors

@handle_errors
def search_element(element, by, keyword):
    """Search element with selenium driver. If element is not found, it return "not-found", 
    otherwise, it returns a webdriver element.

    Args:
        - element (webdriver.Element)
        - by (webdriver.By)
        - keyword (str): Key word to search for

    Return:
        - webdriver.Element or "not-found"
    """
    return element.find_element(by, keyword)

@handle_errors
def search_element_by_key_attribute(element, by, keyword, attribute, value):
    elements = element.find_elements(by, keyword)
    for element in elements:
        if element.get_attribute(attribute) == value:
            return element

@handle_errors
def search_elements_by_key_attribute(element, by, keyword, attribute, value):
    elements_list = list()
    elements = element.find_elements(by, keyword)
    for element in elements:
        if element.get_attribute(attribute) == value:
            elements_list.append(element)
    return elements_list