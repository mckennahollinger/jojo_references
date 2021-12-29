import requests
from bs4 import BeautifulSoup as bs

# Stands first appear in Part 3 of JoJo and have been in the series since
parts = dict({
3: 'Stardust_Crusaders', 
4: 'Diamond_Is_Unbreakable',
5: 'Vento_Auero',
6: 'Stone_Ocean',
7: 'Steel_Ball_Run',
8: 'JoJolion'})
link = 'https://jojowiki.com/Template:Part_{}_Stand_Table'
fileName = '{}.html'

# Initialize arrays to store info like urls for each part being accessed, Stand users and their Stand names
# TODO: make arrays into a dictionary that holds Stand user, Stand name and what part they're from based on arc being iterated upon
# stands = []
# users = []

stand = {'Part': [], 'Name': [], 'User': []}

def getParts(part):
    # For each part 3-8
    for key in part:
        # Insert the current arc being iterated into str to access table
        url = link.format(key)
        # Append that url to the array storing urls
        # urls.append(link)
        # Request url for this part
        r = requests.get(url)
        # Pass into bs4 to access HTML
        soup = bs(r.text, 'html.parser')
        print(soup)

        tags = soup.find_all('div', {'class': 'diamond charname'})

        # #Write and save each arc's Stand table to its own html file
        # with open(fileName.format(parts[key]), "w", encoding='utf-8') as file:
        #     file.write(str(soup))

def getStands(part):
    # For each part 3-8
    for num, key in enumerate(part):
        # Open each part's Stand table from its respective, local html file
        with open(fileName.format(part[key]), encoding='utf-8') as file:
            # Read data from each part's Stand table
            data = file.read()

            # Convert raw text data into parsable HTML
            soup = bs(data, 'html.parser')

            # Access each individual Stand's tile within table
            # Switch find to find_all when finding all Stands from part
            stand_tiles = soup.find('div', {'class': 'charbox diamond resizeImg'})
            
            # Access details about each Stand within each tile
            stand_info = stand_tiles.find('div', {'class': 'charname'}).find_all('a')

            # For each tag providing information about current Stand
            for idx,tag in enumerate(stand_info):

                #First <a href> title is the Stand i.e title = Star Platinum
                if(idx == 0):
                    stand['Part'].append(num+3)
                    stand_name = tag['href']
                    stand_name = stand_name.replace('_', ' ')
                    stand_name = stand_name.replace('/', '')

                    # Multiple Stand names with '&' that appear as ASCII
                    if '%26' in stand_name:
                        stand_name = stand_name.replace('%26', '&')

                    stand['Name'].append(stand_name)

                #Second <a href> title is the Stand user i.e title = Jotaro Kujo
                elif(idx == 1):
                    stand_user = tag['href']
                    stand_user = stand_user.replace('_', ' ')
                    stand_user = stand_user.replace('/', '')
                    stand['User'].append(stand_user)
    print(stand)

# getParts(parts)
getStands(parts)


#TODO: Do I even need these?
standsURL = []
usersURL = []
refs = []
musicRef = []

#Change str to access specific Stand user's page
#TODO: after getting program to run properly again implement reference as part of dictionary
# str = 'https://jojowiki.com{}'

# #Go through each Stand user's specific profile page to grab Stand name reference
# for stand in stands:
#     #Insert the current character being iterated into str to access table
#     url = str.format(stand)
#     #Request url for this character
#     r = requests.get(url)
#     #Pass into bs4 to access HTML
#     soup = bs(r.text, 'html.parser')
#     #Accesses specific Stand user's HTML table where reference is stored
#     tags = soup.find_all('div', {'class': 'pi-data-value pi-font'})
#     #<a href="/The_Star" class="mw-redirect" title="The Star">The Star</a>
#     #Above should be correct by accessing the inner HTML
#     # for tag in tags.find_all('span', {'class': 'noresizeimg wdark wlight supalt'}):
#     #     print(tag)


