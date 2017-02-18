import urllib
from bs4 import BeautifulSoup
import requests
import re

url = 'http://bip.parzeczew.nv.pl/Article/id,510.html'
#fhand = urllib.urlopen('http://bip.parzeczew.nv.pl')

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

#print soup.find_all("a", class_="button-download")
for tag in soup.find_all("a", class_="button-download"):
    #print tag.attrs
    file_to_get = tag.get('href')
    print tag.get('href')
    get_filename = re.findall('([0-9]*).html', file_to_get)
    filename = get_filename[0]
    print filename

    #Downloading files
    urllib.urlretrieve(file_to_get, 'files/'+filename+'.pdf')
    print 'Plik files/'+filename+'.pdf zostal zapisany'


    '''img = urllib.urlopen(file_to_get)
    fhand = open(filename+'.pdf', 'w')
    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1 : break
        size = size + len(info)
        fhand.write(info)
    print size,'characters copied.'
    fhand.close()'''


# Retrieve all of the anchor tags
#tags = soup('ul')
#for tag in tags:
    #print tag.attrs
    #print 'URL:',tag.get('href', None)
    #print tag.get('class', None)

#soup.find_all("a", "menu")
