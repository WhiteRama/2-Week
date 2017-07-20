# -*- coding: utf-8 -*-
# above allow writing "Korean" at source code.

import pandas as pd
import numpy as np
import re
import os

def extract_food_list(file_name):
    # Read CSV File and get rawData which column`s name are a ~ i, header + 7 days.
    rawData = pd.read_csv(file_name, names=['a','b','c','d','e','f','g','h','i'])

    # Initialize empty string.
    food_candidate = ""

    # ignore english and number.
    for a in rawData.c:
        # 월요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.d:
        # 화요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.e:
        # 수요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.f:
        # 목요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.g:
        # 금요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.h:
        # 토요일
        food_candidate = append_food_candidate(food_candidate, a)

    for a in rawData.i:
        # 일요일
        food_candidate = append_food_candidate(food_candidate, a)

    food_candidate = parsing_food_candidate(food_candidate)

    # initialize empty list to append food_list.
    food_list = []
    food_input = []

    # accept '\n' and split list with '\n'
    for food in food_candidate:
        # if '\n' appear, append input.
        if len(food) < 2:
            food_list.append(food_input)
            food_input = []
        # if not '\n', append it.
        else:
            food_input.append(food)

    # delete enter and only one list.
    a = 0
    while a < len(food_list):
        # delete '\n' whcih length is 1.
        if len(food_list[a]) < 2:
            del food_list[a]
        else:
            a += 1
    
    # Delete other exception string.
    for food in food_list:
        a = 0
        while a < len(food):
            # Delete "원".
            if len(food[a]) < 3:
                del food[a]
            # Delete ends with "요일".
            elif food[a].endswith("\xbf\xe4\xc0\xcf"):
                del food[a]
            # Delte ~~) which is changed to escape.
            elif 'escape' in food[a]:
                del food[a]
            else:
                a += 1

    # initialize food input and return values.
    food_input = []
    food_merged = []
    for food in food_list:
        # if food is only one, add to food_input.
        # else, add it to food_merged.
        if len(food) > 1:
            food_merged.append(food_input)
            food_merged.append(food)
            food_input = []
        else:
            food_input += food
    
    a = 0
    while a < len(food_merged):
        if len(food_merged[a]) < 1:
            del food_merged[a]
        else:
            b = 0
            # \xec\x8c\x80\xeb\xb0\xa5 : 쌀밥
            while b < len(food_merged[a]):
                if food_merged[a][b].startswith('\xec\x8c\x80\xeb\xb0\xa5'):
                    if not food_merged[a][b].endswith('\xec\x8c\x80\xeb\xb0\xa5'):
                        f_temp = food_merged[a][b]
                        del food_merged[a][b]
                        food_merged[a].append('\xec\x8c\x80\xeb\xb0\xa5')
                        food_merged[a].append(f_temp.split('\xec\x8c\x80\xeb\xb0\xa5')[-1])
                    else:
                        b += 1
                else:
                    b += 1
            a += 1

    a = 0
    while a < len(food_merged):
        if len(food_merged[a]) < 1:
            del food_merged[a]
        else:
            a += 1

    return food_merged

def print_food(food_list):
    '''
    print korean food list in Korean(euc - kr) not unicode or utf8.
    Args : food_list - to print out food list.
    Returns : nothing.
    '''
    for food in food_list:
        print("==========================length : " + str(len(food)) + "=================================")
        for food_a in food:
            print("length : " + str(len(food_a)) + '\t: ' + food_a.decode('cp949'))
            # We can print korean with decode('cp949') or ('euckr')
        print("========================Next Food List===============================")

def append_food_candidate(food_cand, a):
    '''
    append string with a at given food candidate, food_cand.
    '''
    # Delete english and number at string.
    food_cand += re.sub('[a-z|A-Z|0-9]', '', str(a))
    food_cand += '\n'
    return food_cand

def parsing_food_candidate(food_cand):
    '''
    ignore given signs or blank, ( ** ).
    '''
    # ignore any sign.
    food_candidate = re.sub('[\{\}\[\]\/?.,;:|*~`!^\-_+@\#$%&\\\=\'\"><]','', food_cand)

    # ignore any blank
    food_candidate = re.sub(' |\t','', food_candidate)

    # ignore ( ** ) or start with ( and finish with ) string.
    food_candidate = re.sub('\(.*.*\)|\(.*','', food_candidate)
    # Don`t change to '', because of parsing evalid...
    food_candidate = re.sub('.*\)','escape', food_candidate)

    food_candidate = food_candidate.split("\n")

    return food_candidate

def search_dir(dir_location):
    dir_list = []
    dir_candidate = os.listdir(dir_location)
    for dirr in dir_candidate:
        if os.path.isdir(dir_location + '/' + dirr):
            dir_list.append(dir_location + '/' + dirr)
    return dir_list

def search_file(dir_location):
    '''
    Search all not directory files in dir_location.
    Args : dir_location - directory location where we want to find files.
    Returns : file_list - file name list which have full path.
    '''
    file_list = []
    file_candidate = os.listdir(dir_location)
    for f in file_candidate:
        if os.path.isfile(dir_location + '/' + f):
            file_list.append(dir_location + '/' + f)
    return file_list

def word_classifier(food_l):
    '''
    Count word at once. And how many word were apeared.
    '''
    word_list = []
    word_number = []
    for food in food_l:
        for f in food:
            # if not in word_list, new food word is appeard.
            # Gathered it.
            if f not in word_list:
                word_list.append(f)
                word_number.append(1)
            else:
                word_number[word_list.index(f)] += 1
    return word_list, word_number


# comment : http://pinkwink.kr/958 http://snowple.tistory.com/271 http://ruriro.tistory.com/13 
# file_name = '/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/test.csv'
# /home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/Etable_csv

dir_list = search_dir('/home/sshrik/vacation project/Lab Study/2/2-Week/ChoiHyunJoonProject/4 week code/Etable_csv')

food_list = []

for dir_el in dir_list:
    file_list = search_file(dir_el)
    for f in file_list:
        food_candidate = extract_food_list(f)
    food_list += food_candidate

# print_food(food_list)
word_list, word_number = word_classifier(food_list)

for a in range(0, len(word_list)):
    print(word_list[a].decode('cp949') + " is " + str(word_number[a]))

print "All food number is " + str(len(word_list)) + " & " + str(len(word_number))
print "finished extracting."