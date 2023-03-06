from selenium import webdriver
import chromedriver_autoinstaller

# auto install chromedriver
from selenium.webdriver.common.by import By

chromedriver = chromedriver_autoinstaller.install()

# driver define and lunch
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()


# Go to website and get email

def get_meta(web_element, prop):
    for e in web_element.find_elements(by=By.TAG_NAME, value='meta'):
        if e.get_attribute('itemprop') == prop:
            return e.get_attribute('content')
    return None


def get_track_ids(url):
    driver.get(url)
    z = driver.find_element(by='id', value='tlTab')

    for i in range(1, int(get_meta(z, 'numTracks'))):
        for t in z.find_elements(by=By.CLASS_NAME, value=f'trRow{i}'):
            print(get_meta(t, 'url').split('/')[2])
            print(get_meta(t, 'name'))


get_track_ids(url='https://www.1001tracklists.com/tracklist/24dcb6mk/vintage-culture-culture-shock-078-2023-03-03.html')
# get_track_ids(url='https://www.1001tracklists.com/tracklist/2fqbr4jk/yotto-tomorrowland-friendship-mix-2023-02-23.html')

driver.close()
