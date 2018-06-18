'''
Test for evaluating compatibility of littlesoup with requests
'''
import requests
import time
from littlesoup import LittleSoup
from bs4 import BeautifulSoup

# xpath: /html/body/div[1]/div/div/div/p[2]
# session = requests.Session()
# response = session.get('https://sis.ashesi.edu.gh')
with open('test2.html', 'r') as htmlfile:
    htmlcontent = htmlfile.read()
print("Done loading page")

soups = [LittleSoup, BeautifulSoup]
soup_names = ["LittleSoup", "BeautifulSoup"]
num = 1

for i, soup in enumerate(soups):
    print(f"Testing {soup_names[i]}:")
    start = time.time()
    for j in range(num):
        if soup is LittleSoup:
            # lsoup = soup(response.content, response.encoding)
            lsoup = soup(htmlcontent)
        else:
            # bsoup = soup(response.content, 'html.parser')
            bsoup = soup(htmlcontent, 'html.parser')
    end = time.time()
    print(f"Number of Runs: {num}\nAverage Time:{(end-start)/num}\n\n")

print(lsoup.div.attrs)
print(lsoup.div.attrs)
# print("With little: ")
# print(lsoup.find('a', {'href': 'https://daily.bandcamp.com/2018/06/08/kadhja-bonet-childqueen-album-review/'}))
#
# print("\n\nWith Beauty: ")
# print(bsoup.find('a', {'href': 'https://daily.bandcamp.com/2018/06/08/kadhja-bonet-childqueen-album-review/'}))


# lsoup = LittleSoup(response.content, response.encoding)
# bsoup = BeautifulSoup(response.content, 'html.parser')
# print(bsoup.find('a', {'href': '#discover/'}))

# xpath: /html/body/div[3]/div/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a
# print(lsoup.body.find('a', {'href': '#/discover'}))

# with open('test2.html', 'r') as htmlfile:
#     htmlcontent = htmlfile.read()
# lsoup = LittleSoup(htmlcontent)
# bsoup = BeautifulSoup(htmlcontent, 'html.parser')
# print(lsoup.find('img').attrs)
# print(bsoup.find('img').attrs)

# with open('test.html', 'r') as htmlfile:
#     htmlcontent = htmlfile.read()
# lsoup = LittleSoup(htmlcontent)
# print(lsoup.find('select', {'name': 'side_mp'}))

# soup = LittleSoup(response.content, response.encoding)
# string = soup.html.body.div__1.div.div.div.p__2.string
# print(type(string))
