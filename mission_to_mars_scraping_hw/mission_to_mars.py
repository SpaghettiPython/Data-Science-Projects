import urllib3
from splinter import Browser 
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import cssutils

mars_dict = {}

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def nasa_text():
    try:
        browser = init_browser()
        nasa_url = 'https://mars.nasa.gov/news/'
        browser.visit(nasa_url)
        # * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.
        # Assign the text to variables that you can reference later.
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')
        news_title = soup.find('div', class_='content_title').find('a').text
        news_paragraph = soup.find('div', class_='article_teaser_body').text
        # print(news_title)
        # print(news_paragraph)
        mars_dict['news_title'] = news_title
        mars_dict['news_paragraph'] = news_paragraph
    finally:
        browser.quit()



### JPL Mars Space Images - Featured Image

# * Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

# * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

# * Make sure to find the image url to the full size `.jpg` image.

# * Make sure to save a complete url string for this image.

# ```python
# # Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
# ```

def mars_images():
    try:
        browser = init_browser()
        space_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(space_images_url)
        image_html = browser.html

        # Parse HTML with Beautiful Soup
        soup1 = bs(image_html, 'html.parser')
        # print(soup2.prettify())


        image_alt="""<div class_="carousel_item" style="background-image: url('/spaceimages/images/wallpaper/PIA09113-1920x1200.jpg');" />"""
        soup2 = bs(image_alt, 'html.parser')
        div_style = soup2.find('div')["style"]
        style = cssutils.parseStyle(div_style)
        image_url = style['background-image']
        image_url = image_url.replace('url(', '').replace(')', '')
        # print(image_url)
        main_space_image_url = space_images_url[:25]
        final_image_url = main_space_image_url + image_url
        # print(final_image_url)
        mars_dict['final_image_url'] = final_image_url
        return mars_dict
    finally:
        browser.quit()


# ### Mars Weather

# * Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

# ```python
# # Example:
# mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
# ```


def mars_weather():
    try:
        browser = init_browser()
        mars_weather_url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(mars_weather_url)



        # * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.
        # Assign the text to variables that you can reference later.
        weather_html = browser.html
        # Parse HTML with Beautiful Soup
        soup3 = bs(weather_html, 'html.parser')
        print(soup3.prettify())



        weather_report = soup3.find_all('div', class_='js-tweet-text-container')
        weather_tweet_list = []
        weather_report
        for i in weather_report:
            weather_tweet_list.append(i.find("p").text)
        weather_tweet = weather_tweet_list[3][8:74]
        mars_dict["weather_tweet"] = weather_tweet
        return mars_dict
    finally:
        browser.quit()


# ### Mars Facts

# * Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

# * Use Pandas to convert the data to a HTML table string.


def mars_facts():

# * Use Pandas to convert the data to a HTML table string.
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(mars_facts_url)
    mars_facts_df = pd.DataFrame(mars_facts[1])
    mars_facts_df.columns = ["Description", "Mars_facts"]
    mars_facts_df.set_index("Description", inplace=True)
    data = mars_facts_df.to_html()
    mars_dict["mars_facts_df"] = data
    return mars_dict



# ### Mars Hemispheres

# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
def mars_hemispheres():
    try:
        browser = init_browser()
        mars_weather_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(mars_weather_url)



        images_html = browser.html

        # Parse HTML with Beautiful Soup
        soup4 = bs(images_html, 'html.parser')
        print(soup4.prettify())



        items = soup4.find_all('div', class_='item')
        hemisphere_image_urls = []
        hemispheres_image_url = 'https://astrogeology.usgs.gov'

        for i in items:
            browser = init_browser()
            #Titles
            title = i.find('h3').text
            img_urls = i.find('a', class_='itemLink product-item')['href']
            #IMG Urls
            browser.visit(hemispheres_image_url + img_urls)
            img_html = browser.html
            soup = bs(img_html, 'html.parser')
            img_url = hemispheres_image_url + soup.find('img', class_='wide-image')['src']
            hemisphere_image_urls.append({"title": title, "img_url": img_url})

        mars_dict["mars_hemispheres"] = hemisphere_image_urls
        return mars_dict
    finally:
        browser.quit()
