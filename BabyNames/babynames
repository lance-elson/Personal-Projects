# Scraping baby names, gender association, geographic origin
# and englicised meaning
#
# Author: Lance Elson
#
# In the works. Lots of good stuff to come.
#
# TBA:
# 1) go through all pages for each letter, for now only
# looking at main pages
# 2) optimize list of names copy used for url navigation
# 3) add data to a table
# 4) likely generate ENTIRE list of names before scraping. would be faster

from bs4 import BeautifulSoup
from urllib.request import urlopen
# TBA:

# Manually adjustable alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm','n', 'o','p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Going through each letter of the alphabet
for letter in alphabet:

    url = "https://www.babynames.com/names/" + letter
    page = urlopen(url)

    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # extracting name text from html
    namehtml = soup.find_all('div', class_="namesindex")
    namestext = namehtml[0].getText()
    namestext = namestext.splitlines()
    namestext = list(filter(None, namestext))

    # cleaning list of names
    n = range(0,len(namestext))
    for index in n:
        namestext[index] = namestext[index].strip()
    
    # making a copy of names to replace special characters for url
    # navigation
    # *** To-do: make namestextcopy ignore case, replace all lowercase
    # special characters ***
    namestextcopy = namestext
    for index in n:
        namestextcopy[index] = namestext[index].replace(' ', '%2B')
        namestextcopy[index] = namestext[index].replace('é', 'e')
        namestextcopy[index] = namestext[index].replace('Ç', 'c')
        namestextcopy[index] = namestext[index].replace('í', 'i')

    # scraping individual name web pages
    for currentname in namestextcopy:
        # TBA: make this look at name from original namestext list
        url = "https://www.babynames.com/name/" + currentname
        page = urlopen(url)

        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        desc = soup.find_all('div', class_='name-meaning')
        gender = desc[0].getText()
        origin = desc[1].getText()
        meaning = desc[2].getText()
        print(currentname)
        print(gender)
        print(origin)
        print(meaning)
    