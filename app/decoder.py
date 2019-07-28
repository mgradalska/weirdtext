import re


class IncorrectInputException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Incorrect input detected!')


class Decoder():
    def __init__(self, separator='\n-weird-\n'):
        self.separator = separator

    def __read_input(self, input_data):
        regex = re.compile(r'^{0}([\s\S]*?){0}([\s\S]*?)'.format(self.separator))
        if regex.match(str(input_data)):
            return input_data
        else:
            raise IncorrectInputException()

    def decode_text(self, text):
        input_text = self.__read_input(text)
        encoded_text, real_words = self.__split_input_into_parts(input_text)
        encoded_words = re.findall(r'(\w+)', encoded_text)
        return self.__replace_encoded_words_in_text(encoded_text, encoded_words, real_words)

    def __replace_encoded_words_in_text(self, text, encoded_words, real_words):
        for encoded_word in encoded_words:
            for real_word in real_words.split(' '):
                if (sorted(real_word) == sorted(encoded_word)):
                    text = text.replace(encoded_word, real_word)
        return text

    def __split_input_into_parts(self, input_text):
        input_parts = input_text.split(self.separator)
        return input_parts[1], input_parts[2]
