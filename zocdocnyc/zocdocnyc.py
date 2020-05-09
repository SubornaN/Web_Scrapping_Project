from selenium import webdriver
import time
import csv


driver = webdriver.Chrome()

driver.get("https://www.zocdoc.com/profiles/new-york")

## This code will collect urls of the pages

page_url = [(el.get_attribute('href')) for el in driver.find_elements_by_xpath('//div[@class="sc-14mdbn4-0 fMQpmu"]/a')]

## links to all the pages
''' First url is None type, because it is the staring page. 
So, I manually assigned it the main page to not have issues with the for loop. '''

page_url[0] = 'https://www.zocdoc.com/profiles/new-york'


# for loop for collecting all urls
doc_urls = []

for url in page_url:  # for every page urls
    driver.get(url) # go to the url

    # collect url links from that page
    i = [(el.get_attribute('href')) for el in \
         driver.find_elements_by_xpath('//div[@class="sc-2gkh1u-2 dkERYX"]/a')]
    
    # add the links to this variable
    doc_urls.extend(i)
    
    time.sleep(2) # stay on every page for 3 seconds


# for loop for collecting info on every doctors
name = []
specialties = []
overall_rating = []
total_reviews = []
wait_time = []
manner = []
language = []
gender = []
city = []
zipcode = []

for durl in doc_urls:
    
    driver.get(durl)

    #############################################################

    n = [el.text for el in driver.find_elements_by_xpath('//span[@data-uem-id="provider-name"]')]

    if n == []:
        name.append(None)
    else:
        name.append(n)

    #############################################################

    s = [el.text for el in driver.find_elements_by_xpath('//h2[@class="sc-9yjfx1-12 mdZQO"]')]
    
    if s == []:
        specialties.append(None)
    else:
        specialties.append(s)
    
    #############################################################
    
    o = [el.text for el in driver.find_elements_by_xpath\
    ('//div[@data-test="reviews-section-header-rating-0"]//div[@data-test="star-rating-score"]')]
    
    if o == []:
        overall_rating.append(None)
    else:
        overall_rating.extend(o)
    
    #############################################################
    
    t = [el.text for el in driver.find_elements_by_xpath\
                 ('//div[@class="sc-9yjfx1-9 guXVFG"]//button[@data-test="header-review-link"]')]
    
    if t == []:
        total_reviews.append(None)
    else:
        total_reviews.extend(t)
    
    #############################################################
    
    w = [el.text for el in driver.find_elements_by_xpath\
             ('//div[@data-test="reviews-section-header-rating-1"]//div[@data-test="star-rating-score"]')]
    
    if w == []:
        wait_time.append(None)
    else:
        wait_time.extend(w)
    
    #############################################################
    
    m = [el.text for el in driver.find_elements_by_xpath\
          ('//div[@data-test="reviews-section-header-rating-2"]//div[@data-test="star-rating-score"]')]
    
    if m == []:
        manner.append(None)
    else:
        manner.extend(m)
    
    #############################################################



    
    g = [el.text for el in driver.find_elements_by_xpath('//section[@data-test="Sex-section"]/p')]
    
    if g == []:
        gender.append(None)
    else:
        gender.extend(g)

    
    #############################################################
    

    l = [el.text for el in driver.find_elements_by_xpath('//section[@data-test="Languages-section"]/ul')]
    
    if l == []:
        language.append(None)
    else:
        language.append(l)
    
    
    #############################################################
    
    c = [el.text for el in driver.find_elements_by_xpath('//div[@elementtiming="Header"]//h2[@data-test="header-location"]')]
    
    if c == []:
        city.append(None)
    else:
        city.append(c)
    
    #############################################################
    
    z = [el.text for el in driver.find_elements_by_xpath('//div[@data-test="location-card-info"]//p[@data-test="city-state-zip"]//span[@itemprop="postalCode"]')]

    if z == []:
        zipcode.append(None)
    else:
        zipcode.append(z)
    
    time.sleep(2)


info_dict = {'name': name, 
             'specialties': specialties, 
            'overall_rating': overall_rating,
             'total_reviews': total_reviews,
             'wait_time': wait_time,
             'manner': manner,
             'language': language,
             'gender': gender,
             'city': city,
            'zipcode': zipcode}


csv_file = open('zocdocnyc.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
writer.writerow(info_dict.values())


driver.close()




