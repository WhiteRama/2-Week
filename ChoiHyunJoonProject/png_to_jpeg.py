'''
Hello Hello
'''

from PIL import Image
import os

filenames = os.listdir('/home/sshrik/plus_data/train')

for files in filenames:
    im = Image.open('/home/sshrik/plus_data/train/' + files)
    im.save(files.split(".")[0] + ".jpeg")