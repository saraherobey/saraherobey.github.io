from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request
#get all libraries we need.

#store base url for site - for scraping, fixate at root of a tree
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# print(url)
#
# print(url + "/subdomain")


#using that url, get the HTML from it.
html = request.urlopen(url).read()
# print(html[:2000])

#take html we have and turn it into some soup
soup = BeautifulSoup(html, 'lxml')
#prepare tasty dishes!

#take that soup and find all the anchors
links = soup.find_all('a')[0:10]
#finding all the anchor tags (links) could be using any html tags

# print(soup.text[0:2000])
#only give me first 2000 characters

# print(soup.text.replace("\n", " ")[0:1000])
# print(soup.select(".content"))
# for link in soup.select("td.content a"):
#     print(link.text)

# #finding tails to add onto root url
# links_html = soup.select('td.content a')
# #finding content w td tags that have content and anchors?
# urls =[1]
# for link in links_html:
#     #for those links found,
#     url = link['href']
#     #look for links with href?
#     urls.append(url)
#     #take above and make i
# print(urls)

#go thru soup and grab all links we care about (td tags w content class that have anchor tags inside of them)
links_html = soup.select('td.content a')

#make empty list called urls
urls = []

#go thru each url, get rid of 'blob/' and give me a link that adds the sub url to the base url. these will be links that actually work
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)

#creates empty list called corpus text
corpus_texts = []

#for all the things in list urls, go thru them, then print url first (so you know its still working)
for url in urls:
    print(url)

    #opens urls you want then reads them; sending an http request
    html = request.urlopen(url).read()

    #making html we have into somethinng we can use - a
    #bunch of beautiful soup. lxml is a xml parser
    soup = BeautifulSoup(html, "lxml")

    #turns soup into text; (method chain), replace breaks with nothing
    text = soup.text.replace('\n', '')

    #add text data to the growing corpus
    corpus_texts.append(text)

#prints contents of thing so you know it ran
print(corpus_texts)
