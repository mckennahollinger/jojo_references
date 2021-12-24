import requests
from bs4 import BeautifulSoup as bs

#There are 166 unique Stands in total across parts 3-8

arcs = ['3','4','5','6','7','8'] #Parts 1 & 2 don't feature stands, so need parts afterwards
str = 'https://jojowiki.com/Template:Part_{}_Stand_Table'

urls = [] #empty list to append urls for Stands to scrape for references
stands = []
users = []

for arc in arcs:
    count = 0
    if(arc == '3'):
        url = str.format(arc)  # inserts part number into general url
        urls.append(url)
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')

        tags = soup.find_all('div', {'class': 'diamond charname'})

        for tag in tags:
            if (count < 1):
                for anchor in tag.find_all('a'):
                    idx = tag.find_all('a').index(anchor)
                    if (idx == 0):
                        stands.append(anchor['href'])
                    if (idx == 1):
                        users.append(anchor['href'])
                count = count + 1
            else:
                break
        print(stands)
        print(users)
    else:
        break

standsURL = []
usersURL = []
refs = []
musicRef = []

str = 'https://jojowiki.com{}'

for stand in stands:
    url = str.format(stand)
    print(url)
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    tag = soup.find('span', {'class': 'newwin'})
    print(tag)
    # for anchor in tags.find_all('a'):
    #     idx = tags.find_all('a').index(anchor)
    #     if (idx == 0):
    #         refs.append(anchor['href'])

    # for tag in tags.find_all('span', {'class': 'newwin'}):
    #     print(tag)

str = 'https://en.wikipedia.org/wiki/'