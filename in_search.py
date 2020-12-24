import requests
def main():

    print('=====list of topics=====')
    material=['society','science','health','technology','environment']
    i=1
    for c in material:
        print(i,c)
        i+=1

    ask = input('Enter the topic of your choice(id) :')
    iask=int(ask)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r=requests.get("https://www.sciencedaily.com/news/top/"+material[iask-1],headers=headers)
    with open("searches.html","w") as searches:
            searches.write(r.text)
if __name__ == "__main__":
    main()
