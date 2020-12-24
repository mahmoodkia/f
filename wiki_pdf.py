import requests
def main():

    url="https://en.wikipedia.org/api/rest_v1/page/pdf"
    askf=input('Enter your search :')
    respone = requests.get(url+"/"+askf)
    with open('metadata.pdf', 'wb') as f:
        f.write(respone.content)
if __name__=='__main__':
    main()
