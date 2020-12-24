from datetime import date
from bs4 import BeautifulSoup
import at
import speach
def main():
    print('----------Library-----------')
    print('''......List of articles:  ''')
    at.main()
    a = input('enter the id of article you wanna see(1-10): ')
    i = a
    pm = '/home/m/python/articles/'
    with open(pm+'ar'+str(i)+'.html')as afile:
        soup=BeautifulSoup(afile,'lxml')
    today=date.today()
    d=today.strftime("%B %d, %Y")
    tag_title=soup.find('title')
    ts=tag_title.string
    print('''----------------------------------------------------------------------------------------------------------------------------------------------------------\n\n''')
    print('Date : ',d)
    print("*************************************************************************")
    print('Title'.center(4,'='),':',ts)
    print("*************************************************************************")
    #f = open(pm+'ar'+str(i)+'.txt','w')
    tag_text=soup.find('div',id='text')
    content = tag_text.find_all('p')
    print('''----------------------------------------------------------------------------------------------------------------------------------------------------------''')
    for c in (content):
        cs = c.string
        unicode_string=str(cs)
        print(unicode_string,''' ''')
        #speach.st(unicode_string)
    print('''----------------------------------------------------------------------------------------------------------------------------------------------------------''')
    askf=input('Do you want to continue reading?[y/n]:')
    def unkown():
        askf=input('Do you want to continue reading?[y/n]:')
        if askf=='y':
            at.main()
            main()
        elif askf=='n':
            print('Programm closed')
            afile.close()
        else:
            unkown()
    if askf=='y':
        #at.main()
        main()
    elif askf=='n':
        print('closed reading section')
        afile.close()
    else:
        unkown()
if __name__=='__main__':
    main()
