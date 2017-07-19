from bs4 import BeautifulSoup as BS
import urllib2 as ub
import codecs
import re

html_doc = '/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/Eatable/1501/noname.html'
with codecs.open(html_doc, "r", encoding='euc-kr') as f:
    data = f.readlines()

line_data = ""
for line in data:
    line_data = line_data + '\n' + line

# line_data = unicode(line_data, errors='ignore')
# sys.setdefaultencoding('utf-8')

soup = BS(line_data, 'lxml')

# ignore english and number.
food_candidate = re.sub('[a|c-q|s-z|A|B-Q|S-Z|0-9]','',line_data)
# ignore any sign.
food_candidate = re.sub('[\{\}\[\]\/?.,;:|*~`!^\-_+@\#$%&\\\=\'\"]','', food_candidate)
# ignore start with ( and finish with ).
food_candidate = re.sub('[(.*))]','', food_candidate)
# replace <br> or <BR> to \n.
food_candidate = re.sub('<BR>|<br>','\r\n', food_candidate)

# ... Then delete all.
food_candidate = re.sub('[b|r|B|R|>|<]','', food_candidate)


'''
for a in soup.find_all(id='f_8w11s0'):
    print(a.encode('utf-8'))
'''

print(food_candidate)

'''
for i in soup.find_all('td'):
    print(i)
'''