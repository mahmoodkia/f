from bs4 import BeautifulSoup
import re
import csv
def main():

    with open("wikisearch.html",'r') as hfile:
        soup=BeautifulSoup(hfile,'lxml')

    csv_file = open('wiki_linklist.txt','w')
    csv_writer = csv.writer(csv_file)
    data = soup.findAll('div', {'class':'mw-search-result-heading'})


    for div in data:
        links = div.findAll('a')
            #print(links)
        for a in links:

                #print (a['href'])
            csv_writer.writerow(["https://wikipedia.org"+a['href']])


    csv_file.close()
if __name__=='__main__':
    main()
