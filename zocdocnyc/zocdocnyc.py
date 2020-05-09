from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
driver.get("https://www.zocdoc.com/profiles/new-york")



## This code will collect urls of the pages

page_url = [(el.get_attribute('href')) for el in driver.find_elements_by_xpath('//div[@class="sc-14mdbn4-0 fMQpmu"]/a')]

''' First url is None type because it is the staring page. 
So, I manually assigned it the main page to not have issues with the for loop. '''

page_url[0] = 'https://www.zocdoc.com/profiles/new-york'



doc_urls = []
for url in page_url:
    
    driver.get(url) # go to the url

    # collect all links from every page
    links = [(el.get_attribute('href')) for el in driver.find_elements_by_xpath('//div[@class="sc-2gkh1u-2 dkERYX"]/a')]
    
    # add each links to this variable
    doc_urls.extend(links)
    
    time.sleep(2)


## Looping through each link and adding rows to csv file

with open('zocdocnyc.csv', 'w', encoding='utf-8', newline='') as csv_file:

    writer = csv.writer(csv_file)

    for durl in doc_urls:
    # Initialize an empty dictionary for doctor's information

        info_dict = {}

        driver.get(durl)

        #### BACKGROUND
        try:
            name = driver.find_element_by_xpath('//span[@data-uem-id="provider-name"]').text
        except:
            name = 'None'

        try:
            specialties = driver.find_element_by_xpath('//h2[@class="sc-9yjfx1-12 mdZQO"]').text
        except:
            specialties = 'None'

        try:
            gender = driver.find_element_by_xpath('//section[@data-test="Sex-section"]/p').text
        except:
            gender = 'None'

        try:
            language = driver.find_element_by_xpath('//section[@data-test="Languages-section"]/ul').text
        except:
            language = 'None'

        try:
            city = driver.find_element_by_xpath('//div[@elementtiming="Header"]//h2[@data-test="header-location"]').text
        except:
            city = 'None'

        try:
            zipcode = driver.find_element_by_xpath('//div[@data-test="location-card-info"]//p[@data-test="city-state-zip"]//span[@itemprop="postalCode"]').text
        
        except:
            zipcode = 'None'


        ### RATINGS
        
        try:
            total_reviews = driver.find_element_by_xpath('//div[@class="sc-15uikgc-2 elchZz"]').text
        except:
            total_reviews = 'None'

        try:
            overall_rating = driver.find_element_by_xpath\
            ('//div[@data-test="reviews-section-header-rating-0"]//div[@data-test="star-rating-score"]').text
        except:
            overall_rating = 'None'

        try:
            wait_time = driver.find_element_by_xpath\
            ('//div[@data-test="reviews-section-header-rating-1"]//div[@data-test="star-rating-score"]').text
        except:
            wait_time = 'None'

        try:
            manner = driver.find_element_by_xpath\
            ('//div[@data-test="reviews-section-header-rating-2"]//div[@data-test="star-rating-score"]').text
        except:
            manner = 'None'

        try:
            video_visit = driver.find_element_by_xpath('//div[@class="sc-1anfxv2-3 dtGxOU"]').text == 'Video visit'
        except:
            video_visit = False

        info_dict['name'] = name
        info_dict['specialties'] = specialties
        info_dict['gender'] = gender
        info_dict['language'] = language
        info_dict['city'] = city
        info_dict['zipcode'] = zipcode
        info_dict['overall_rating'] = overall_rating
        info_dict['total_reviews'] = total_reviews
        info_dict['wait_time'] = wait_time
        info_dict['manner'] = manner
        info_dict['Video_Visit'] = video_visit
        info_dict['doc_urls'] = durl

        writer.writerow(info_dict.values())

        time.sleep(2)

#csv_file.close()
driver.close()








