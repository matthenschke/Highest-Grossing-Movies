from bs4 import BeautifulSoup
import requests
import re
from csv import writer


# get the highest-grossing movies of all time

# get html of page
response = requests.get('https://www.imdb.com/list/ls000021718/') 
html = response.text

# set up web scraper
soup = BeautifulSoup(html, 'html.parser')

# get DOM elements
main_container = soup.find('div', id = "wrapper").find('div', id = "root") # main container
list_container = main_container.find('div', class_ = "lister-list") # list container
lists = list_container.findAll('div', class_ = "lister-item mode-detail") # get all lists

with open('highest_grossing_movies.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Rank', 'Gross', 'Name']
    csv_writer.writerow(headers)
    # iterate through all lists and print out the movie name and gross
    for i in range(len(lists)):
        list_content = lists[i].find('div', class_ = "lister-item-content") # content for each list
        rank = re.sub('[.]', '', list_content.find('span').string) # movie rank
        gross = lists[i].find('div', class_ = "list-description").find('p').string # gross 
        movie_name = list_content.find('a').string # movie name
        csv_writer.writerow([rank, gross, movie_name])

    
    
    


