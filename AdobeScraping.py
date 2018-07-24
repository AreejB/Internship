import bs4
import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://adobe.wd5.myworkdayjobs.com/external_experienced/30/refreshFacet/318c8bb6f553100021d223d9780d30be"

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")



data = page_soup.findAll('div',attrs={"class":"gwt-Label WBUO"})

data = page_soup.findAll('span',attrs={"class":"gwt-InlineLabel WK-F WJYF"})

data = page_soup.find(id="gwt-uid-2")

data = page_soup.findAll('div', {'class': 'gwt-Label WBUO'})
print (data)
