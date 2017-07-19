import csv
from collections import defaultdict

mat = []

f = open('/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/noname.csv', 'r')
#csvReader = csv.reader(f, delimiter=',')
csvReader = csv.DictReader(f)

'''
for row in csvReader:
    print(row)
    for r in row:
        print(r.decode('euckr').encode('utf-8'))
    print("==Next Line==")
'''

columns = defaultdict(list)
for row in csvReader:
    for (k, v) in enumerate(row):
        columns[k].append(v)
print(len(columns))
for i in columns:
    print("%d th columns." %i)
    for st in columns[i]:
        try:
            print(st.decode('euckr').encode('utf-8'))
        except AttributeError:
            print("AttributeError occured...")
f.close()