"""앞서 뽑아낸 Streamed Tweets 파일에서 가장 많이 쓰인 단어를 WordCloud로 나타낸 프로그램"""
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
from konlpy.tag import Kkma
kkma = Kkma()

# loading streamed file
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
# print(new_lines)

# 1. making word cloud which shows most-used words
# extracting out sentences which is not ''
sentences = [line for line in new_lines if line != '']

# analyzing each sentence with using Kkma
morpheme_list = []
for sentence in sentences:
    morpheme_list.append(kkma.pos(sentence))
# print(morpheme_list)

# picking up words
word_list = []
for morpheme in morpheme_list:
    for word, tag in morpheme:
        if tag in ['VV', 'VXV', 'NNG', 'NNB', 'NNM', 'NNP', 'VA', 'VAX']: # nouns, verbs, adjs
            word_list.append(word)

# counting most-used words
most_used_words = Counter(word_list)

# making word cloud
wordcloud = WordCloud(width=900, height=600,
                  font_path="C:\Windows\Fonts\HoonPinkpungchaR.otf",
                  background_color='white')
cloud = wordcloud.fit_words(most_used_words)
plt.figure(figsize=(15, 20))
plt.axis('off')
plt.imshow(cloud)
plt.show()