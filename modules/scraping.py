from modules.selenium_module import WeatherScraper
import time
def list_all_station(webscraper:WeatherScraper):
    '''
    function to return list of all stations
    '''
    txt_station_element = webscraper.get_element('id','cityname')
    # webscraper.change_text(dropdown_station,'Ang Mo Kio')
    station_parent_element = webscraper.get_next_element('parent',txt_station_element)[0]
    # print(station_parent_element.get_attribute('outerHTML'))
    dropdown_station_class = webscraper.get_next_element('child',station_parent_element)[1]
    list_of_station_element = webscraper.get_next_element('child',dropdown_station_class)
    result = []
    for el in list_of_station_element:
        link_element = webscraper.get_next_element('child',el)[0]
        # print(link_element.get_attribute('outerHTML'))
        link_element_text = link_element.get_attribute('innerText')
        result.append(link_element_text)
    print('All possible stations:')
    print(result)
    print() #new line
    return result

def click_dropdown_option(webscraper:WeatherScraper, 
                          element_id,
                          input):
    '''
    function to interact with dropdown menu button
    '''
    is_option_available = False
    txt_element = webscraper.get_element('id',element_id)
    parent_element = webscraper.get_next_element('parent',txt_element)[0]
    dropdown_class = webscraper.get_next_element('child',parent_element)[1]
    list_element = webscraper.get_next_element('child',dropdown_class)
    for el in list_element:
        link_element = webscraper.get_next_element('child',el)[0]
        link_element_text = link_element.get_attribute('innerText')
        if link_element_text==input:
            is_option_available=True
            break
    if is_option_available:
        txt_element.click()
        time.sleep(0.5)
        el.click()
    return is_option_available