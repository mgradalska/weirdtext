from django.test import TestCase

from app.decoder import Decoder, IncorrectInputException
from app.encoder import Encoder

decoder = Decoder()
encoder = Encoder()


class EncoderTestCase(TestCase):
    def test_when_encodes_returns_correct_sorted_words(self):
        original_text = 'some (text) for, test!'
        encoder_result = encoder.create_encoded_response(original_text)
        sorted_string = encoder_result.split('\n-weird-\n')[2]
        assert sorted_string == 'for some test text'

    def test_encodes_with_default_separator(self):
        original_text = 'some? text|| for, test'
        encoder_result = encoder.create_encoded_response(original_text)
        assert '\n-weird-\n' in encoder_result

    def test_when_empty_string_returns_separators(self):
        original_text = ''
        encoder_result = encoder.create_encoded_response(original_text)
        assert encoder_result == '\n-weird-\n\n-weird-\n'

    def test_when_numer_input_encodes_correctly(self):
        original_text = 123
        encoder_result = encoder.create_encoded_response(original_text)
        assert encoder_result == '\n-weird-\n123\n-weird-\n123'

    def test_when_custom_separator_returns_correct_response(self):
        original_text = 'some text for test'
        custom_separator = '--separator--'
        custom_encoder = Encoder(custom_separator)
        encoder_result = custom_encoder.create_encoded_response(original_text)
        assert custom_separator in encoder_result


class DecoderTestCase(TestCase):
    def test_when_decodes_returns_correct_string(self):
        encoded_text = '\n-weird-\nsmoe expmale txet\n-weird-\nexample some text'
        decoded = decoder.decode_text(encoded_text)
        assert decoded == 'some example text'

    def test_when_missing_first_separator_raises_exception(self):
        encoded_text = 'smoe expmale txet\n-weird-\nexample some text'
        self.assertRaises(IncorrectInputException)
        with self.assertRaises(IncorrectInputException):
            decoder.decode_text(encoded_text)

    def test_when_missing_second_separator_raises_exception(self):
        encoded_text = '\n-weird-\nsmoe expmale txetexample some text'
        self.assertRaises(IncorrectInputException)
        with self.assertRaises(IncorrectInputException):
            decoder.decode_text(encoded_text)

    def test_when_missing_separator_raises_exception(self):
        encoded_text = 'smoe expmale txetexample some text'
        self.assertRaises(IncorrectInputException)
        with self.assertRaises(IncorrectInputException):
            decoder.decode_text(encoded_text)

    def test_when_error_in_separator_raises_exception(self):
        encoded_text = '\n-weird-\nsmoe expmale txet\n-weirxxd-\nexample some text'
        self.assertRaises(IncorrectInputException)
        with self.assertRaises(IncorrectInputException):
            decoder.decode_text(encoded_text)

    def test_decodes_with_custom_separator(self):
        custom_separator = '--separator--'
        encoded_text = '--separator--smoe expmale txet--separator--example some text'
        custom_decoder = Decoder(custom_separator)
        decoded = custom_decoder.decode_text(encoded_text)
        assert decoded == 'some example text'


class EncoderAndDecoderTestCase(TestCase):
    def test_when_encodes_end_decodes_returns_the_same(self):
        text = 'some example test text'
        encoded = encoder.create_encoded_response(text)
        decoded = decoder.decode_text(encoded)
        assert decoded == text
