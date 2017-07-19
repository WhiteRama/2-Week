import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# http://pinkwink.kr/958
rawData = pd.read_csv('/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week \
code/test.csv', names=['a','b','c','d','e','f','g','h','i'], encoding='euckr')

food_candidate = ""

# ignore english and number.
for a in rawData.c:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.d:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.e:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.f:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.g:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.h:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

for a in rawData.i:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

# ignore any sign.
food_candidate = re.sub('[\{\}\[\]\/?.,;:|*~`!^\-_+@\#$%&\\\=\'\"><]','', food_candidate)

# ignore any blank
food_candidate = re.sub(' |\t','', food_candidate)

# ignore ( ** ) or start with ( and finish with ) string.
food_candidate = re.sub('\(.*.*\)|\(.*','', food_candidate)
food_candidate = re.sub('.*\)','<escape>', food_candidate)

food_candidate = food_candidate.split("\n")

food_list = []
food_input = []

# accept '\n' and split list with '\n'

for food in food_candidate:
    if len(food) < 2:
        food_list.append(food_input)
        food_input = []
    else:
        food_input.append(unicode(food))

a = 0
while a < len(food_list):
    if len(food_list[a]) == 0:
        del food_list[a]
    else:
        a += 1

for food in food_list:
    for food_a in food:
        print(food_a.encode('utf8'))
    print("Next Food List...")