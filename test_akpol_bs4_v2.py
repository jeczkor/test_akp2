#!/usr/bin/python
#new_branch
#new_branch2

dane = { 'submit':'Login',
         'myusername':'',
         'mypassword':'',
         'co':'a%%',
         'button':'szukaj'}


import requests
import subprocess
from bs4 import BeautifulSoup
import MySQLdb
import csv


c = requests.session()
x = c.post("http://81.95.207.234/poznan/checklogin.php", data=dane)
z = c.post("http://81.95.207.234/poznan/dostepnosc.php", data=dane)
out = z.text
out2 = out.encode('utf-8')
out2 = out2.replace("</tr><td>","</tr><tr><td>")
out2 = out2.replace("</tr> <td>","</tr><tr><td>")
soup = BeautifulSoup(out2)
table1 = soup.find('table')
#table2 = table1.findAll("tr")
#table3 = table2.findAll("td")
rows = table1.findAll('tr')
file = open("test_out_bs4.csv","w")

for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = ''.join(td.find(text=True))
        text = text.encode('utf-8')
        file.write(text+";")
#        print text+";",
    file.write("\n")
file.close()







