import numpy as np


class Generator(object):
    def __init__(self):
        self.ind_words = []
        self.pair = ()
        self.word_dict = {}
        self.first_word = ""
        self.chain = []
        self.n_words = 20

    def make_pairs(self, ind_words):
        for i in range(len(ind_words) - 1):
            yield (ind_words[i], ind_words[i + 1])

    def fit(self, data):
        data = data.replace('\n', ' ')
        self.ind_words = data.split(' ')
        self.pair = self.make_pairs(self.ind_words)

        for word_1, word_2 in self.pair:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

    def generate(self, n_words=20):
        self.first_word = np.random.choice(self.ind_words)
        while self.first_word.islower():
            self.first_word = np.random.choice(self.ind_words)
        self.n_words = n_words
        self.chain = [self.first_word]
        for i in range(self.n_words):
            if '.' in self.chain[-1] and i > (self.n_words // 2):
                break
            if self.chain[-1] in self.word_dict:
                self.chain.append(np.random.choice(self.word_dict[self.chain[-1]]))
            else:
                break

        return ' '.join(self.chain)


data = open('/Users/sergei/PycharmProjects/Tcode/input.txt', encoding='utf8').read()

model = Generator()
model.fit(data)

print(model.generate(100))
