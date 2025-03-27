from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=').text 
soup = BeautifulSoup(html_text,'lxml')
