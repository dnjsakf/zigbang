from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tmon_parser( response=None, **kwargs ):
    wait_time = 30 if kwargs.get('wait_time') is None else int(kwargs.get('wait_time'))
    count = 10 if kwargs.get('count') is None else kwargs.get('count')
    
    # Element를 찾을 때까지 N초간 대기, 이전에 찾으면 종료.
    items = WebDriverWait(response, wait_time).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="_dealList"]/li[position() <= {}]/a'.format( count )))
    )

    datas = list()
    for no, item in enumerate( items ):
        link = item.get_attribute('href')
        title = item.find_element_by_xpath('div/div[3]/p[2]')
        price = item.find_element_by_xpath('div/div[3]/div[1]/span[1]/span/i')

        datas.append( {
            "no": no+1
            , "title": title.text.strip()
            , "price": price.text.replace(',', '').strip()
            , "link": link.strip()
            , "request_url": response.current_url
        })
    return datas

def st11_parser( response=None, **kwargs ):
    wait_time = 30 if kwargs.get('wait_time') is None else int(kwargs.get('wait_time'))
    count = 10 if kwargs.get('count') is None else kwargs.get('count')

    # Element를 찾을 때까지 N초간 대기, 이전에 찾으면 종료.
    items = WebDriverWait(response, wait_time).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="emergencyPrd"]/div/ul/li[position() <= {}]/div/a'.format( count )))
    )

    datas = list()
    for no, item in enumerate( items ):
        link = item.get_attribute('href')
        title = item.find_element_by_xpath('div[3]/p/span')
        price = item.find_element_by_xpath('div[3]/div/span[2]/strong')

        datas.append( {
            "no": no+1
            , "title": title.text.strip()
            , "price": price.text.replace(',', '').strip()
            , "link": link.strip()
            , "request_url": response.current_url
        })
    return datas

def wemap_parser( response=None, **kwargs ):
    wait_time = 30 if kwargs.get('wait_time') is None else int(kwargs.get('wait_time'))
    count = 10 if kwargs.get('count') is None else kwargs.get('count')

    # Element를 찾을 때까지 N초간 대기, 이전에 찾으면 종료.
    items = WebDriverWait(response, wait_time).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="_contents"]/div/div[2]/div[4]/div[3]/div/a[position() <= {}]'.format( count )))
    )
    
    datas = list()
    for no, item in enumerate( items ):
        link = item.get_attribute('href')
        title = item.find_element_by_xpath('div/div[2]/div[2]/p')
        price = item.find_element_by_xpath('div/div[2]/div[2]/div/div[2]/strong/em')

        datas.append( {
            "no": no+1
            , "title": title.text.strip()
            , "price": price.text.replace(',', '').strip()
            , "link": link.strip()
            , "request_url": response.current_url
        })
    return datas