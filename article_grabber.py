import requests
import csv
import os
import shutil
from pathlib import Path
def main():
    i = 1
    with open("linklist.txt",'r') as omega:
        content=omega.readlines()
        #print(content)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    content=map(lambda s: s.strip(), content)
    pm = "/home/m/python/articles/"
    if i < 10:
        for url in content:
            if i < 11:
                #print(url)
                page = requests.get(url,headers=headers)
                print('loading the article' + str(i))
                f = open("ar"+str(i)+'.html','w')
                f.write(page.text)
                f.close()
                shutil.move('ar'+str(i)+".html",pm+'ar'+str(i)+".html")
                i = i+1
            else:
                print("Done")

if __name__=='__main__':
    main()
