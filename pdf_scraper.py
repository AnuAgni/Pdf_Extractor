import pandas as pd
import re
import urllib.parse
from urllib.parse import unquote
from bs4 import BeautifulSoup
import requests


url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1234/"
 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
 
i=0 
sno=[]
pdf_links=[]


for link in links:
    if ('.pdf' in link.get('href', [])):
        initial_url=link.get('href')
        if not re.match('(?:http|ftp|https)://', initial_url):
            url_string = urllib.parse.unquote(initial_url)
            header_url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1234/"
            new_link = "".join((header_url,url_string))
            f_url=urllib.parse.quote_plus(new_link)
            pdf_url = unquote(f_url)
            #pdf_url=urllib.parse.quote(new_link)
        else:
            pdf_url=initial_url
        i+=1
        sno.append(i)
        pdf_links.append(pdf_url)
        
df=pd.DataFrame({'S.no.':sno,'Link':pdf_links})
df.to_csv('pdf_links.csv',index=False)

