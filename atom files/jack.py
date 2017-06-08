from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/881019.html"

corpus_texts = []

html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'lxml')

print(soup('p'))

# paragraphs = soup.find('p')
#
# corpus_texts.append(paragraphs)
#
# text = soup.text.replace('\n', '')
#
# corpus_texts.append(text)
#
#
#
# print(corpus_texts)
