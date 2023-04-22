from bs4 import BeautifulSoup
import requests
url = "https://theprint.in/"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html)

headline = soup.find_all('h3', class_ = 'entry-title td-module-title')
for tag in headline:
    print(tag.get_text())
