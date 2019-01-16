{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Web Scraping and Document Databases Homework"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Part 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1 - Scraping\n",
    "\n",
    "# Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.\n",
    "\n",
    "# Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping \n",
    "# and analysis tasks. The following outlines what you need to scrape."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. \n",
    "# Assign the text to variables that you can reference later.\n",
    "\n",
    "# Example:\n",
    "# news_title = \"NASA's Next Mars Mission to Investigate Interior of Red Planet\"\n",
    "# news_p = \"Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, \n",
    "# on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary \n",
    "# launch in history from America's West Coast.\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://mars.nasa.gov/news/?page=0'\n",
    "response = requests.get(url)\n",
    "soup = bs(response.text, 'html.parser')\n",
    "# print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "results = soup.find(class_=\"slide\")\n",
    "# results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_title = results.find(class_=\"content_title\").text\n",
    "news_p = results.find(class_=\"rollover_description_inner\").text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nIn deploying its first instrument onto the surface of Mars, the lander completes a major mission milestone.\\n'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "news_title\n",
    "# news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# JPL Mars Space Images - Featured Image\n",
    "\n",
    "# Visit the url for JPL Featured Space Image here. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\n",
    "\n",
    "# Use splinter to navigate the site and find the image url for the current Featured Mars Image and \n",
    "# assign the url string to a variable called featured_image_url.\n",
    "# Make sure to find the image url to the full size .jpg image.\n",
    "# Make sure to save a complete url string for this image.\n",
    "\n",
    "# Example:\n",
    "# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from splinter.exceptions import ElementDoesNotExist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "url1 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "response1 = requests.get(url1)\n",
    "soup1 = bs(response1.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [],
   "source": [
    "articles = soup1.footer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<footer>\n",
       "<a class=\"button fancybox\" data-description=\"Scientists produced new global maps of Jupiter using the Wide Field Camera 3 on NASA's Hubble Space Telescope. One color map is shown here, projected onto a globe and as a flat image.\" data-fancybox-group=\"images\" data-fancybox-href=\"/spaceimages/images/mediumsize/PIA19643_ip.jpg\" data-link=\"/spaceimages/details.php?id=PIA19643\" data-title=\"Spinning Jupiter and Global Map\" id=\"full_image\">\n",
       "\t\t\t\t\tFULL IMAGE\n",
       "\t\t\t\t  </a>\n",
       "</footer>"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "articles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA19643_ip.jpg\n"
     ]
    }
   ],
   "source": [
    "link = articles.find('a')\n",
    "href = link['data-fancybox-href']\n",
    "print('https://www.jpl.nasa.gov' + href)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_url = 'https://www.jpl.nasa.gov' + href"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather (Twitter) - https://twitter.com/marswxreport?lang=en\n",
    "# class_= js-tweet-text-container\n",
    "# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page.\n",
    "#    - http://space-facts.com/mars/\n",
    "# Save the tweet text for the weather report as a variable called mars_weather.\n",
    "\n",
    "# Example:\n",
    "# mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url2 = 'https://twitter.com/marswxreport?lang=en'\n",
    "response2 = requests.get(url2)\n",
    "soup2 = bs(response2.text, 'html.parser')\n",
    "# print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [],
   "source": [
    "articles = soup2.find(class_='js-tweet-text-container')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_weather = articles.find('p').text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sol 2288 (2019-01-12), high -7C/19F, low -68C/-90F, pressure at 8.23 hPa, daylight 06:45-18:55pic.twitter.com/Or8q1l3tka'"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Facts - https://space-facts.com/mars/\n",
    "# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet \n",
    "# including Diameter, Mass, etc.\n",
    "# Use Pandas to convert the data to a HTML table string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url3 = 'https://space-facts.com/mars/'\n",
    "response3 = requests.get(url3)\n",
    "soup3 = bs(response3.text, 'html.parser')\n",
    "# print(soup3.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "url = 'https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                  -153 to 20 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Metric</th>\n",
       "      <th>Mars Measurement</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Metric               Mars Measurement\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.42 x 10^23 kg (10.7% Earth)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.52 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                  -153 to 20 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = tables[0]\n",
    "df.columns = ['Metric', 'Mars Measurement']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars Measurement</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Metric</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                   Mars Measurement\n",
       "Metric                                             \n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.42 x 10^23 kg (10.7% Earth)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.52 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                  -153 to 20 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.iloc[1:]\n",
    "df.set_index('Metric', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_html('mars_facts.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This part is optional as the website is not working\n",
    "# Mars Hemispheres - USGS site - https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\n",
    "\n",
    "# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.\n",
    "# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.\n",
    "# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title \n",
    "# containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.\n",
    "# Append the dictionary with the image url string and the hemisphere title to a list. \n",
    "# This list will contain one dictionary for each hemisphere.\n",
    "\n",
    "# Example:\n",
    "# hemisphere_image_urls = [\n",
    "#     {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"...\"},\n",
    "#     {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"...\"},\n",
    "#     {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"...\"},\n",
    "#     {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"...\"},\n",
    "# ]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 2 - MongoDB and Flask Application\n",
    "\n",
    "# Notes: mars | safe}\n",
    "\n",
    "# Use MongoDB with Flask templating to create a new HTML page that displays all of the information \n",
    "# that was scraped from the URLs above.\n",
    "\n",
    "# Start by converting your Jupyter notebook into a Python script called scrape_mars.py \n",
    "# with a function called scrape that will execute all of your scraping code from above \n",
    "# and return one Python dictionary containing all of the scraped data.\n",
    "\n",
    "# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.\n",
    "\n",
    "# Store the return value in Mongo as a Python dictionary.\n",
    "\n",
    "# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.\n",
    "# Create a template HTML file called index.html that will take the mars data dictionary \n",
    "# and display all of the data in the appropriate HTML elements. \n",
    "# Use the following as a guide for what the final product should look like, but feel free to create your own design."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# news_title\n",
    "# news_p\n",
    "# featured_image_url\n",
    "# mars_weather\n",
    "# mars_facts.html"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
