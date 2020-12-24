from bs4 import BeautifulSoup
def main():
    pm='/home/m/python/articles/'
    i=1
    while i < 11:
        with open(pm+"ar"+str(i)+".html") as afile:
            soup=BeautifulSoup(afile,'lxml')
        f=open(pm+'ar'+str(i)+'.txt','w')
        tag_text=soup.find('div',id='text')
        content= tag_text.find_all('p')
        for c in content:
            cs=c.string
            unicode_string= str(cs)
            f.write(unicode_string)

        f.close()
        i= i +1


if __name__=='__main__':
    main()
