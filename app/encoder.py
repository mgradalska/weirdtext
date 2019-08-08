import re
from random import shuffle


class Encoder:
    def __init__(self, separator='\n-weird-\n'):
        self.separator = separator

    def _fetch_words(self, text):
        return re.findall(r'(\w+)', text)

    def _encode_text(self, text, words):
        encoded_words = self._encode_words(words)
        encoded_text = text
        for index, word in enumerate(words):
            encoded_text = encoded_text.replace(word, encoded_words[index], 1)
        return encoded_text

    def create_encoded_response(self, text):
        text = str(text)
        words = self._fetch_words(text)
        encoded_text = self._encode_text(text, words)
        sorted_words = self._sort_words(words)
        return self.separator + encoded_text + self.separator + sorted_words

    def _encode_words(self, words):
        encoded_words = []
        for word in words:
            encoded_words.append(self._shuffle_word(word))
        return encoded_words

    def _shuffle_word(self, word):
        middle = list(word[1:-1])
        if len(set(middle)) > 1:
            while middle == list(word[1:-1]):
                shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        else:
            return word

    def _sort_words(self, words):
        return ' '.join(sorted(words, key=lambda word: word.lower()))
