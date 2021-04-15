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
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Manually adjustable alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm','n', 'o','p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
# Going through each letter of the alphabet
    for currentletter in alphabet:

        url = "https://www.babynames.com/names/" + currentletter
        page = urlopen(url)

        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
    
        # extracting name text from html
        namehtml = soup.find_all('div', class_="namesindex")
        namestext = namehtml[0].getText()
        namestext = namestext.splitlines()
        namestext = list(filter(None, namestext))

        # cleaning whitespace from list of names
        n = range(0,len(namestext))
        for index in n:
            namestext[index] = namestext[index].strip()
    
        # making a copy of names to replace special characters for url
        # navigation
        namestextcopy = namestext
        for index in n:
            namestextcopy[index] = namestext[index].lower()
            namestextcopy[index] = namestext[index].replace(' ', '%2B')
            namestextcopy[index] = namestext[index].replace('á', 'a')
            namestextcopy[index] = namestext[index].replace('ç', 'c')
            namestextcopy[index] = namestext[index].replace('ë', 'e')
            namestextcopy[index] = namestext[index].replace('é', 'e')
            namestextcopy[index] = namestext[index].replace('í', 'i')
            namestextcopy[index] = namestext[index].replace('ó', 'o')
            namestextcopy[index] = namestext[index].replace('ü', 'u')
            namestextcopy[index] = namestext[index].replace('ú', 'u')

    # scraping individual name web pages
        for currentname in namestextcopy:
            url = "https://www.babynames.com/name/" + currentname
            page = urlopen(url)

            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")

            header = soup.find_all('h1', class_="baby-name")
            desc = soup.find_all('div', class_='name-meaning')
            name = header[0].getText()
            gender = desc[0].getText()
            origin = desc[1].getText()
            meaning = desc[2].getText()
            print(name)
            print(gender)
            print(origin)
            print(meaning)
            writer.writerows([name,gender,origin,meaning])
