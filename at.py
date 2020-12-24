from bs4 import BeautifulSoup
def main():

    i=1
    while i < 11:
        with open('/home/m/python/articles/'+"ar"+str(i)+".html") as afile:
            soup=BeautifulSoup(afile,'lxml')




        #tag_head = soup.find('p',id='first',class_="lead")
        #print(tag_head.string)
        tag_title=soup.find ('title')

        ts=tag_title.string
        print(str(i)+'.',ts)
        i+=1
        afile.close()
        #main()

if __name__ == "__main__":
    main()
