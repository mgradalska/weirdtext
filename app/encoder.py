import re
from random import shuffle


class Encoder():
    def __init__(self, separator='\n-weird-\n'):
        self.separator = separator

    def __fetch_words(self, text):
        return re.findall(r'(\w+)', text)

    def __encode_text(self, text, words):
        encoded_words = self.__encode_words(words)
        encoded_text = text
        for index, word in enumerate(words):
            encoded_text = encoded_text.replace(word, encoded_words[index], 1)
        return encoded_text

    def create_encoded_response(self, text):
        text = str(text)
        words = self.__fetch_words(text)
        encoded_text = self.__encode_text(text, words)
        sorted_words = self.__sort_words(words)
        return self.separator + encoded_text + self.separator + sorted_words

    def __encode_words(self, words):
        encoded_words = []
        for word in words:
            encoded_words.append(self.__shuffle_word(word))
        return encoded_words

    def __shuffle_word(self, word):
        middle = list(word[1:-1])
        if len(set(middle)) > 1:
            while middle == list(word[1:-1]):
                shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        else:
            return word

    def __sort_words(self, words):
        sorted_string = ''
        for idx, word in enumerate(sorted(words)):
            sorted_string += word + ' ' if idx != len(words) - 1 else word
        return sorted_string
