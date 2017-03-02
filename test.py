import urllib
from bs4 import BeautifulSoup
#import requests
import re

url_to_get = ['http://bip.parzeczew.nv.pl/Article/get/id,15344.html', 'http://bip.parzeczew.nv.pl/Article/get/id,15341.html']
#fhand = urllib.urlopen('http://bip.parzeczew.nv.pl')

def get_url_to_get(url):


def get_uchwaly(url):

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    #print soup.find_all("a", class_="button-download")
    pliki = soup.find_all("div", class_="line-row")

    for item in pliki:

        #print item
        print '-------------------------'

        text = item.find("p").get_text()
        text = text.encode('utf-8')
        print text

        attrib = item.find_all("span")
        #format = text.encode('utf-8')
        file_size = attrib[0].get_text()
        file_date_add = attrib[1].get_text()
        file_format = attrib[2].get_text()
        print file_size
        print file_date_add
        print file_format

        a = item.find("a").get('href')
        a = a.encode('utf-8')
        #href = a["href"]
        print a

    print '______________________________'
    print 'Pobrano pozycji: ', len(pliki)
    print '______________________________'
    #print(dd.pretiffy())

for url in url_to_get:
    get_uchwaly(url)

#print soup.select("div.line-row p")
#print soup.select("a.button-download")
#for tag in soup.find_all("div", class_="line-row"):
    #print tag.attrs
    #type(tag)
'''file_to_get = tag.get('href')
    print tag.get('href')
    get_filename = re.findall('([0-9]*).html', file_to_get)
    filename = get_filename[0]
    print filename

    #Downloading files
    #urllib.urlretrieve(file_to_get, 'files/'+filename+'.pdf')
    print 'Plik files/'+filename+'.pdf zostal zapisany'

img = urllib.urlopen(file_to_get)
    fhand = open(filename+'.pdf', 'w')
    size = 0
    while True:
        info = img.read(100000)
        if len(info) < 1 : break
        size = size + len(info)
        fhand.write(info)
    print size,'characters copied.'
    fhand.close()



# Retrieve all of the anchor tags
#tags = soup('ul')
#for tag in tags:
    #print tag.attrs
    #print 'URL:',tag.get('href', None)
    #print tag.get('class', None)

#soup.find_all("a", "menu")
'''
