# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import urllib2 as ub
import sys

html_doc = '/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/Eatable/1501/noname.html'
with open(html_doc, 'r') as f:
    data = f.readlines()

line_data = ""
for line in data:
    line_data += line

line_data.decode('cp949').encode('utf-8')
# sys.setdefaultencoding('utf-8')
soup = BS(line_data, 'html.parser')
print(soup.tr)