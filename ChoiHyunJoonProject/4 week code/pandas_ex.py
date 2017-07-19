import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# http://pinkwink.kr/958
rawData = pd.read_csv('/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week \
code/test.csv', names=['a','b','c','d','e','f','g','h','i'], encoding='euckr')
print(rawData.c)

food_candidate = ""

# ignore english and number.
for a in rawData.c:
    food_candidate += re.sub('[a-z|A-Z|0-9]','',unicode(a))
    food_candidate += u'\n'

# ignore any sign.
food_candidate = re.sub('[\{\}\[\]\/?.,;:|*~`!^\-_+@\#$%&\\\=\'\"><]','', food_candidate)

food_candidate = re.sub('\(.*.*\)|\(.*','', food_candidate)
food_candidate = re.sub('.*\)','<escape>', food_candidate)

print(food_candidate)
