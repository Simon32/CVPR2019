import requests
from bs4 import BeautifulSoup

url="http://openaccess.thecvf.com/CVPR2019.py"
html=requests.get(url)

soup=BeautifulSoup(html.content)

soup.a.contents=='pdf'

pdfs=soup.findAll(name="a",text="pdf")


folder_path='./CVPR2019/'
for i in range(len(pdfs)):
    c=requests.get('http://openaccess.thecvf.com/'+pdf['href']).content
    with open(folder_path+str(i)+'.pdf',mode="wb") as f:
        f.write(c)
        print(str(i)+"finish")
