
from bs4 import BeautifulSoup
import urllib.request

OUTPUT_FILE_NAME = 'output.txt'
URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=052&aid=0001030608'

def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    source = source_code_from_URL.read()
    source_code_from_URL.close()
    
    #soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding = 'utf-8')
    
    text = ""
    for item in soup.fine_all('div', {id : 'articleBodyContents'}):
        text = text + str(item.fine_all(text = True))
    return text

def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()

main()
    
