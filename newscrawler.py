
from bs4 import BeautifulSoup
import urllib.request
import re

OUTPUT_FILE_NAME = 'output.txt'
URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=052&aid=0001030608'
#URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=055'\
#     '&aid=0000445667'

def get_text(URL):
    source_URL = urllib.request.urlopen(URL)
    print("source_URL : ")
    print(source_URL)
    source = source_URL.read()
    
    soup = BeautifulSoup(source, 'lxml', from_encoding = 'utf8')
    text = ''
    for item in soup('div', id = 'articleBodyContents'):
        text = text + str(item.find_all(text = True))
    return text

def get_article(text):
    article = re.sub('[a-zA-Z]','',text)
    article = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]','', article)
    return article

def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    print(result_text)
    result_text = get_article(result_text)
    print()
    print("article : ")
    print(result_text)
    open_output_file.write(result_text)
    open_output_file.close()

if __name__ == '__main__':
    main()
    
