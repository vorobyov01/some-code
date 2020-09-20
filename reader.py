import json
import re


def make_pairs(ind_words):
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])


filename = 'input.txt'
file = open(filename, 'rt', encoding='utf8')
text = file.read()
file.close()

words = re.split(r'\W+', text)
word_dict = {}

pair = make_pairs(words)
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

json.dump(word_dict, open("dict.txt", "w", encoding='utf8'))
