# Imports and download necessary package
# !pip install bs4  #  Download BeautifulSoup library for Web Scraping.
# !pip install lxml  # parser for html.
# !pip install pandas

import pandas as pd
from bs4 import BeautifulSoup

# Import local simple web page 
# Specify the web page below and use tags to filter the data.
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')  # create a soup object and specify parser method.
    # print(soup.prettify())

    # find method only finds the first element and stops the search

    # first_tags = soup.find('h5') 
    # print(tags)

    # find all tags using soup.find_all() passed in the argument

    courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)
    dicty = {}
    # Print just the text inside the tags.
    for course in courses_html_tags:
        # print(course.text)
        dicty[course.text] = []
    # print(dicty)

    # find all div tags
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        # print(course.text)
        course_name = course.h5.text
        # print(course_name)
        course_price = course.a.text.split()[-1]
        # print(course_price)
        dicty[course_name] = (course_price)

    # print(dicty)

    # print the scraped data
    for k,v in dicty.items():
        print(f'Price of {k} on xyz website is {v}.')

# Create a datafram from scraped dictionary so it can be saved as csv
df = pd.DataFrame([(k,v) for k,v in dicty.items()], columns=["Course_name", "Course_price"])
df.index.name = "Sr.No"
df.to_csv("Scraped_data.csv")
print(df)