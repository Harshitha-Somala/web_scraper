from urllib import request
#!python3.10
import requests
from bs4 import BeautifulSoup

# Data for URL
job = "data+science+internship"
Location = "Noida%2C+Uttar+Pradesh"
url = "https://in.indeed.com/jobs?q="+job+"&l="+Location


search_urls = [
    url
]

pages = [
    requests.get(r_url) for r_url in search_urls
]

soups = [
    BeautifulSoup(page.content, "html.parser") for page in pages
]

with open('readme.html', 'w') as f:
    f.write(str(soups))
