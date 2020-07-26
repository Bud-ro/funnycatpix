from bs4 import BeautifulSoup
import os
import urllib.request
import re

#Takes pages to download and scrapes the images into catpics
def main(pages):
    for page in pages:
        url = 'https://www.funnycatpix.com/pictures_' + str(page) + '.htm'
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
        content = urllib.request.urlopen(req)
        webContent = content.read()
        print(f'Read page {page}')
        soup = BeautifulSoup(webContent, features='html.parser')
        li = soup.find_all('li')[:24] #24 elements containing the links
        a = [elem.a for elem in li]
        links = [elem.get('href') for elem in a]
        imageLinks = [_.replace('.htm','.jpg') for _ in links]
        print('Extracted links from the page')
        
        #Iterate through each image link and download it to the catpics folder.
        for link in imageLinks:
            req = urllib.request.Request(link, headers={'User-Agent' : "Magic Browser"})
            content = urllib.request.urlopen(req)
            webContent = content.read()
            print(f'Downloaded {link}')
            fileName = re.search(r'(?<=/)\w+.jpg',link)[0]
            path = 'catpics\\' + fileName
            with open(path,'wb') as f:
                f.write(webContent)
                print(f'Wrote {path}')
        
#Just in case I'm stupid enough to import this.
if __name__ == '__main__':
#range(2,5) #List of pages to scrape
    main(range(3,10))