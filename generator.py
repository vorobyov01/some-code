import numpy as np
import json


class Generator(object):
    def __init__(self):
        self.js = open("dict.txt").read()
        self.word_dict = json.loads(self.js)
        self.ind_words = list(self.word_dict.keys())
        self.pair = ()
        self.first_word = ""
        self.chain = []
        self.n_words = 20

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


model = Generator()
print(model.generate(200))
