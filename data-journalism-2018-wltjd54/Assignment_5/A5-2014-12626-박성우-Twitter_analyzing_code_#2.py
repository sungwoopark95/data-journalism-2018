"""앞서 뽑아낸 Streamed Tweets 파일에서 특정 명사가 총 몇 번 쓰였는지를 알아보기 위한 프로그램"""
import numpy as np
from konlpy.tag import Kkma
kkma = Kkma()

# open txt file
with open('twitter_file.txt', 'r', encoding='utf8') as f:
    lines = f.read().splitlines()

# eliminating Retweet Notation
new_lines = []
for i in range(len(lines)):
    if 'RT' in lines[i]:
        replace_rt = lines[i].replace('RT', '') # eliminating 'RT'
        replace_at = replace_rt.replace('@', '') # eliminating '@'
        split_line = replace_at.split(':') # splitting text from id
        new_line = split_line[1] # picking up text
    else:
        new_line = lines[i]
    new_lines.append(new_line)
sentences = [line for line in new_lines if line != '']

# picking up nouns - without repetition
# use kkma.nouns - making each sentence into a whole
whole = [" ".join(sentences)]
noun_list = kkma.nouns(whole[0])
noun_dict = {noun: i for i, noun in enumerate(noun_list)} # making index

# making occur matrix
occurs = np.zeros([len(sentences), len(noun_list)]) # 1st parameter: row / 2nd parameter: column
np.shape(occurs)

# filling values in occur matrix
for i, sent in enumerate(sentences):
    for noun in noun_list:
        if noun in sent:
            index = noun_dict[noun] # index == i, the numbered index of the noun
            occurs[i][index] = 1

# making co-occurrence matrix
co_occurs = occurs.T.dot(occurs)
total_occur = []
for i in range(len(co_occurs[0])):
    total_occur.append(co_occurs[i][i])
# it shows how many times each word was used in the entire text file
print(total_occur)