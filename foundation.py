#             in the name of god
"""

#project:foundation

"""

print('''
|----------------------------------------------------------------------|
|                                                                      |
|                                                                      |
|     #######                                                          |
|     #        ####  #    # #    # #####    ##   ##### #  ####  #    # |
|     #       #    # #    # ##   # #    #  #  #    #   # #    # ##   # |
|     #####   #    # #    # # #  # #    # #    #   #   # #    # # #  # |
|     #       #    # #    # #  # # #    # ######   #   # #    # #  # # |
|     #       #    # #    # #   ## #    # #    #   #   # #    # #   ## |
|     #        ####   ####  #    # #####  #    #   #   #  ####  #    # |
|                                                                      |
|----------------------------------------------------------------------|''')
print('---------------------'+"""/||\ Wlc to the foundation /||\ -------------------""")

######imports######
import in_search
import search_bs
import article_grabber
import armaker
import arshower
import wiki_pdf
import speach
sector=['1:wikipedia','2:sciencedaily']
tasks=['1:Read articles','2:Update the articles','8:Help','9:About','0:Exit']
def base():
    print("=============the main page=============")
    for s in sector:
        print(s)
        #speach.st(s)
    ask_first=input('enter the sector id(1-2) : ')
    if ask_first =='1':
        print('wiki sector')
        wiki_pdf.main()
        base()
    elif ask_first =='2':



        for t in tasks:
            print(t)
            #speach.st(t)
        askt=input('what task you want me to do : ')
        if askt == "1":
            arshower.main()

            aske=input('Do you wanna go back to main menu?[y/n]')
            if aske == 'n':
                print('Have a nice day!')
            else:
                base()
        elif askt == '2':
            in_search.main()
            search_bs.main()
            article_grabber.main()
            armaker.main()
            base()
        elif askt == '8':
            print(" run the update command first time you use the programm,this command grab new articles\n and shows you latest news,we suggest you do it once in a while to get updated news\n also you have to manually go to files:{armaker,article_grabber,arshower} and then manually change path\n Note:you must create articles folder and put it as path in (pm) variable.\n Note:Running new upgrade overwrite the previous articles, in case you want to save them,\n backup the files located at articles folder(ar.txt files) or add backup functionality used in the code(disable by default)\n")
            base()
        elif askt=='9':
            print("project foundation is an open source project as for now a concept module for our ML module which uses different science websites such as\nscience daily or wiki pedia, we also want to have a minimal human intraction with our machine\nthis platform aim to be both a tool to manange for our modules via single file and maintaining some intraction with our future ML module")
            base()
        elif askt=='0':
            print('Have a nice day!')
        else:
            print('command not found!')
            print('hint choose the id of command you want program to do, ex,1 or 2')
            base()
base()
