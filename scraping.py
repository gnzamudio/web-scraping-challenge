import pandas as pd
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Latest Mars news
    news_url= 'https://redplanetscience.com/'
    browser.visit(news_url)
    time.sleep(5)
    mars_html= browser.html
    soup= bs(mars_html, 'html.parser')


    #Scrape Latest News for title
    newstitle=soup.find('div', class_='content_title').text
    print(newstitle)

    #Scrape for paragraph text
    newstext= soup.find('div', class_='article_teaser_body').text
    print(newstext)

    #Featured Space image
    image_url='https://spaceimages-mars.com/'
    browser.visit(image_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    featured_image_url= "https://spaceimages-mars.com/image/featured/mars1.jpg"
    
    #Facts
    facts_url= 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)
    mars_df=pd.read_html(facts_url)[0]


    #Hemespheres
    hemespheres_url= 'https://marshemispheres.com/'
    browser.visit(hemespheres_url)
    hemespheres_html= browser.html
    soup= bs(hemespheres_html, 'html.parser')
    
    hemURL=soup.find_all('div', class_= 'item')
    hemURL_dict=[]
    for result in hemURL:
        title = result.h3.text
        href = result.find("a")["href"]
        hemisphere_image_url = f"https://marshemispheres.com/{href}"
        browser.visit(hemisphere_image_url)
        h_html = browser.html
        soup = soup = bs(h_html, 'html.parser')
        hemisphere_image_url = soup.find("img", class_="wide-image").get("src")
        hemURL_dict.append({"title": title, "img_url": f"https://marshemispheres.com/{hemisphere_image_url}"})

    

    browser.quit()
    
    return hemURL_dict





