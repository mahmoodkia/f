import requests

asks=input('What are you looking for?:')
r=requests.get("https://en.wikipedia.org/w/index.php?search="+asks+'&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current={}&ns0=1')
with open("wikisearch.html","w") as searches:
        searches.write(r.text)
