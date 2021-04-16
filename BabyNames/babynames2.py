#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 01:20:20 2021

@author: lance
"""

import PyPDF2
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

raw_url_list = []

for i in range(1,246):
    try:
        PDFFile = open("/Users/lance/Downloads/bbnames/" + str(i) + ".pdf",'rb')
     
# this section modified from https://stackoverflow.com/a/56299671
        PDF = PyPDF2.PdfFileReader(PDFFile)
        pages = PDF.getNumPages()
        key = '/Annots'
        uri = '/URI'
        ank = '/A'
        for page in range(pages):
            pageSliced = PDF.getPage(page)
            pageObject = pageSliced.getObject()
            if key in pageObject.keys():
                ann = pageObject[key]
                for a in ann:
                    u = a.getObject()
                    if uri in u[ank].keys():
                        raw_url_list.append(u[ank][uri])
                        
#-----------------------------------------------------------------------------
    
    except:
        pass
                   
           
nameurls = []
for x in raw_url_list:
    x = str(x)
    if (x[0:31] == "https://www.babynames.com/name/"):
        nameurls.append(x)
        
with open('babynames.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
# Going through each letter of the alphabet


    # scraping individual name web pages
    for currenturl in nameurls:
        url = currenturl
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
        writer.writerow([name,gender,origin,meaning])