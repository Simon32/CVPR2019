import requests
from bs4 import BeautifulSoup
import os
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
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
    c=requests.get('http://openaccess.thecvf.com/'+pdf['href'],headers=headers).content
    with open(folder_path+pdf_name,mode="wb") as f:
        f.write(c)
        print('['+str(i)+']'+pdf_name+" finish")






