import requests
from bs4 import BeautifulSoup
import os

url="http://openaccess.thecvf.com/CVPR2019.py"
html=requests.get(url)

soup=BeautifulSoup(html.content)

soup.a.contents=='pdf'

pdfs=soup.findAll(name="a",text="pdf")

if not os.path.exists('./CVPR2019/'):
    os.mkdir('./CVPR2019/') 
folder_path='./CVPR2019/'
for i,pdf in enumerate(pdfs):
    pdf_name=pdf["href"].split('/')[-1]
    c=requests.get('http://openaccess.thecvf.com/'+pdf['href']).content
    with open(folder_path+pdf_name,mode="wb") as f:
        f.write(c)
        print(pdf_name+"finish")






