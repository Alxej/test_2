from word_check import SimilarWordsFinder
from words_parser import WordsParser
import unittest
import os
from unittest.mock import patch


class TestWordsParserPositive(unittest.TestCase):
    true_url = 'https://github.com/nevmenandr/word2vec-russian-novels/tree/master/books_before' # noqa E501
    true_raw_url = 'https://raw.githubusercontent.com/nevmenandr/word2vec-russian-novels/master/books_before' # noqa E501

    def test_get_names_true_url(self):
        true_names = ['CrimeAndPunishment.txt', 'CrimeAndPunishment_JOF.txt',
                      'EugeneOnegin.txt', 'EugeneOnegin_JOF.txt',
                      'FathersAndSons.txt', 'FathersAndSons_JOF.txt',
                      'MasterAndMargarita.txt', 'MasterAndMargarita_JOF.txt',
                      'WarAndPeace.txt', 'WarAndPeace_JOF.txt']
        parsed_names = WordsParser.get_names(self.true_url)
        for name in parsed_names:
            self.assertIn(name, true_names)

    def test_get_text_true_url(self):
        true_text = 'Лабораторная работа номер 1...\n'
        raw_url = 'https://raw.githubusercontent.com/Alxej/testing/refs/heads/main' # noqa E501
        filename = 'README.md'
        parser = WordsParser()
        parsed_text = parser.get_text(filename, raw_url)

        self.assertEqual(true_text, parsed_text)

    def test_write_file_true_parameters(self):
        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        filename = "test_file.txt"
        dictionary = {"data\n": 1}
        parser = WordsParser()
        parser.write_file(filename, dictionary)

        writed = read_data(filename)

        self.assertEqual(writed, 'data - 1\n')

    def test_write_file_empty_data(self):
        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        filename = "test_file.txt"
        dictionary = {"data": 1}
        parser = WordsParser()
        parser.write_file(filename, dictionary)

        writed = read_data(filename)

        self.assertEqual(writed, 'data - 1\n')

    def test_write_file_remove_n_false(self):
        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.read()

        filename = "test_file.txt"
        dictionary = {"data\n": 1}
        parser = WordsParser()
        parser.write_file(filename, dictionary, False)

        writed = read_data(filename)

        self.assertEqual(writed, 'data\n - 1\n')

    @patch("words_parser.WordsParser")
    def test_save_words_and_symbols_true_parameters_block(self,
                                                          mock_parser):
        def test_write_file(filename, data_dict, remove_n=True):
            with open(filename, 'w', encoding="utf-8") as f:
                for key in data_dict.keys():
                    f.write(f"{key.replace("\n", "")} - {data_dict[key]}\n")

        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        mock_parser().write_file.side_effect = test_write_file

        parser = WordsParser()
        symbols_filename = "test_symbols.txt"
        symbols = {'a': 5}
        words_filename = "test_words.txt"
        words = {'awda\n': 10}
        parser.save_words_and_symbols(symbols,
                                      words,
                                      symbols_filename,
                                      words_filename)
        writed_words = read_data(words_filename)
        writed_symbols = read_data(symbols_filename)

        self.assertEqual(writed_words, 'awda - 10\n')
        self.assertEqual(writed_symbols, 'a - 5\n')

    def test_save_words_and_symbols_true_parameters(self):

        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        parser = WordsParser()
        symbols_filename = "test_symbols.txt"
        symbols = {'a': 5}
        words_filename = "test_words.txt"
        words = {'awda\n': 10}
        parser.save_words_and_symbols(symbols,
                                      words,
                                      symbols_filename,
                                      words_filename)
        writed_words = read_data(words_filename)
        writed_symbols = read_data(symbols_filename)

        self.assertEqual(writed_words, 'awda - 10\n')
        self.assertEqual(writed_symbols, 'a - 5\n')

    @patch("words_parser.WordsParser")
    def test_get_unique_words_and_symbols_true_parameters_block(self,
                                                                mock_parser):
        mock_parser().get_names.return_value = ['C.txt', 's.txt'] # noqa E501] # noqa E501
        mock_parser().get_text.return_value = ['just']

        parser = WordsParser()
        words_and_symbols = parser.get_unique_words_and_symbols("", "")
        words = words_and_symbols['words']
        symbols = words_and_symbols['symbols']

        self.assertEqual(len(list(words.keys())), 1)
        self.assertIn('just', list(words.keys()))
        self.assertEqual(words['just'], 2)

        self.assertEqual(len(list(symbols.keys())), 4)
        true_symbols = 'just'.split()
        for s in true_symbols:
            self.assertIn(s, list(symbols.keys()))
            self.assertEqual(symbols[s], 2)

    def test_get_unique_words_and_symbols_true_parameters(self):
        url = 'https://github.com/Alxej/testing_repo/tree/main'
        raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main/README.md' # noqa E501
        parser = WordsParser()
        words_and_symbols = parser.get_unique_words_and_symbols(url, raw_url)
        words = words_and_symbols['words']
        symbols = words_and_symbols['symbols']

        text = '# just life'
        true_words = text.split(' ')
        true_symbols = []
        for word in true_words:
            for s in word.split():
                true_symbols.append(s)

        for word in true_words:
            self.assertIn(word, words.keys())
            self.assertEqual(words[word], 1)

        for sym in true_symbols:
            self.assertIn(sym, symbols.keys())
            self.assertEqual(symbols[sym], 1)

    @patch("words_parser.WordsParser")
    def test_get_unique_words_and_symbols_empty_repository(self, mock_parser):
        mock_parser().get_names.return_value = []

        parser = WordsParser()
        words_and_symbols = parser.get_unique_words_and_symbols("", "")
        words = words_and_symbols['words']
        symbols = words_and_symbols['symbols']

        self.assertEqual(len(list(words.keys())), 0)
        self.assertEqual(len(list(symbols.keys())), 0)

    @patch("words_parser.WordsParser")
    def test_parse_and_save_true_parameters_block(self, mock_parser):
        def write_file(filename, data_dict, remove_n=True):
            with open(filename, 'w', encoding="utf-8") as f:
                for key in data_dict.keys():
                    f.write(f"{key.replace("\n", "")} - {data_dict[key]}\n")

        def test_save_data(dict_of_unique_symbols,
                           dict_of_unique_words,
                           symbols_filename="test_symbols.txt",
                           words_filename="test_words.txt"):
            write_file(symbols_filename,
                       dict_of_unique_symbols)
            write_file(words_filename, dict_of_unique_words)

        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        mock_parser.save_words_and_symbols.side_effect = test_save_data
        mock_parser().get_unique_words_and_symbols.return_value = {
            'words': {'#': 10},
            'symbols': {'#': 10}
        }
        parser = WordsParser()
        parser.parse_and_save("ss", "ss")
        writed_words = read_data("test_words.txt")
        writed_symbols = read_data("test_symbols.txt")
        self.assertEqual(writed_words, '# - 10')
        self.assertEqual(writed_symbols, '# - 10')

    def test_parse_and_save_true_parameters(self):
        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readlines()
        url = 'https://github.com/Alxej/testing_repo/tree/main'
        raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main/README.md' # noqa E501
        parser = WordsParser()
        parser.parse_and_save(url,
                              raw_url,
                              "test_words.txt",
                              "test_symbols.txt")
        writed_words = read_data("test_words.txt")
        writed_symbols = read_data("test_symbols.txt")

        self.assertEqual(writed_words[0], '# - 1')
        self.assertEqual(writed_words[1], 'just - 1')
        self.assertEqual(writed_words[2], 'life - 1')
        self.assertEqual(writed_symbols[0], '# - 1')
        self.assertEqual(writed_symbols[1], 'j - 1')
        self.assertEqual(writed_symbols[2], 'u - 1')
        self.assertEqual(writed_symbols[3], 's - 1')
        self.assertEqual(writed_symbols[4], 't - 1')
        self.assertEqual(writed_symbols[5], 'l - 1')
        self.assertEqual(writed_symbols[6], 'i - 1')
        self.assertEqual(writed_symbols[7], 'f - 1')
        self.assertEqual(writed_symbols[8], 'e - 1')

    @patch("words_parser.WordsParser")
    def test_parse_and_save_empty_repository(self, mock_parser):
        def read_data(filename: str):
            with open(filename, 'r', encoding="utf-8") as f:
                return f.readline()

        mock_parser().get_unique_words_and_symbols.return_value = {
            'words': {},
            'symbols': {}
        }

        parser = WordsParser()
        parser.parse_and_save("ss", "ss")
        writed_words = read_data("words.txt")
        writed_symbols = read_data("symbols.txt")

        self.assertEqual(len(writed_words.keys()), 0)
        self.assertEqual(len(writed_symbols.keys()), 0)


class TestWordsParserNegative(unittest.TestCase):
    def test_get_names_wrong_url(self):
        parser = WordsParser()

        with self.assertRaises(ValueError):
            parser.get_names("sdsadsadasd")

    def test_get_text_wrong_url(self):
        parser = WordsParser()

        with self.assertRaises(ValueError):
            parser.get_text("sdsadsadasd", "sdadsd")

    def test_save_words_and_symbols_wrong_url(self):
        parser = WordsParser()

        with self.assertRaises(ValueError):
            parser.save_words_and_symbols({}, {}, "sdsadsadasd", "sdadsd")

    def test_get_unique_words_and_symbols_wrong_url(self):
        parser = WordsParser()

        with self.assertRaises(ValueError):
            parser.get_unique_words_and_symbols("sdsadsadasd", "sdadsd")


class TestWordCheckPositive(unittest.TestCase):
    true_url = 'https://github.com/Alxej/testing_repo/tree/main' # noqa E501
    true_raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main' # noqa E501
    checker = SimilarWordsFinder(true_url,
                                 true_raw_url,
                                 "words.txt",
                                 'symbols.txt')

    def test_initialize_with_true_parameters(self):
        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "1.txt",
                                     '2.txt')
        self.assertTrue(os.path.exists(checker.symbols_filename))
        self.assertTrue(os.path.exists(checker.words_filename))
        self.assertEqual(checker.symbols_filename, '2.txt')
        self.assertEqual(checker.words_filename, '1.txt')

    def test_get_list_of_words_true_parameters(self):
        checker = self.checker
        words = checker.get_list_of_words()
        true_words = ['#', 'just', 'life']
        for word in true_words:
            self.assertIn(word, words)

    def test_get_list_of_words_empty_file(self):
        checker = self.checker
        words = checker.get_list_of_words('empty.txt')
        self.assertEqual(words, [])

    def test_word_exists_true(self):
        checker = self.checker
        lst = ['s', 'sdasd']
        for s in lst:
            self.assertTrue(checker.word_exists(s, lst))

    def test_word_exists_false(self):
        checker = self.checker

        lst = ['s', 'sdasd']
        self.assertFalse(checker.word_exists('dasdsadsadas', lst))

    @patch('word_check.SimilarWordsFinder')
    def test_get_array_of_words_with_extra_symbol_true_parameters_block(self,
                                                                        mocked_finder): # noqa E501
        def test_word_exists(word, lst):
            return word in lst

        mocked_finder.word_exists.side_effect = test_word_exists

        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "words.txt",
                                     'symbols.txt')
        words = checker.get_array_of_words_with_extra_symbol('wosrd',
                                                             ['word', 'sdas'],
                                                             ['k', 's'])
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'word')

    def test_get_array_of_words_with_extra_symbol_true_parameters(self):
        checker = self.checker
        words = checker.get_array_of_words_with_extra_symbol('wosrd',
                                                             ['word', 'sdas'],
                                                             ['k', 's'])
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'word')

    def test_get_array_of_words_with_extra_symbol_empty_word_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_extra_symbol('wosrd',
                                                             [],
                                                             ['k', 's'])
        self.assertEqual(words, [])

    def test_get_array_of_words_with_extra_symbol_empty_symbol_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_extra_symbol('wosrd',
                                                             ['word', 'sdas'],
                                                             [])
        self.assertEqual(words, [])

    @patch('word_check.SimilarWordsFinder')
    def test_get_array_of_words_with_replaced_symbol_true_parameters_block(self, # noqa E501
                                                                           mocked_finder): # noqa E501
        def test_word_exists(word, lst):
            return word in lst

        mocked_finder.word_exists.side_effect = test_word_exists

        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "words.txt",
                                     'symbols.txt')
        words = checker.get_array_of_words_with_replaced_symbol('word',
                                                                ['wdor', 'sdas'], # noqa E501
                                                                ['k', 's', 'd']) # noqa E501
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'wdor')

    def test_get_array_of_words_with_replaced_symbol_true_parameters(self):
        checker = self.checker
        words = checker.get_array_of_words_with_replaced_symbol('word',
                                                                ['wdor', 'sdas'], # noqa E501
                                                                ['k', 's', 'd']) # noqa E501
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'wdor')

    def test_get_array_of_words_with_replaced_symbol_empty_word_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_replaced_symbol('word',
                                                                [], # noqa E501
                                                                ['k', 's'])
        self.assertEqual(words, [])

    def test_get_array_of_words_with_replaced_symbol_empty_symbol_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_replaced_symbol('word',
                                                                ['dwor', 'sdas'], # noqa E501
                                                                [])
        self.assertEqual(words, [])

    @patch('word_check.SimilarWordsFinder')
    def test_get_array_of_words_with_deleted_symbol_true_parameters_block(self,
                                                                          mocked_finder):  # noqa E501
        def test_word_exists(word, lst):
            return word in lst

        mocked_finder.word_exists.side_effect = test_word_exists

        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "words.txt",
                                     'symbols.txt')
        words = checker.get_array_of_words_with_deleted_symbol('wordd',
                                                                ['word', 'sdas']) # noqa E501
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'word')

    def test_get_array_of_words_with_deleted_symbol_true_parameters(self):
        checker = SimilarWordsFinder(self.true_url,
                                 self.true_raw_url,
                                 "words.txt",
                                 'symbols.txt')
        words = checker.get_array_of_words_with_deleted_symbol('wordd',
                                                                ['word', 'sdas']) # noqa E501
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'word')

    def test_get_array_of_words_with_deleted_symbol_empty_words_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_deleted_symbol('wrd',
                                                                []) # noqa E501
        self.assertEqual(words, [])

    @patch('word_check.SimilarWordsFinder')
    def test_get_array_of_words_with_swapped_symbols_true_parameters_bl(self,
                                                                        mocked_finder):  # noqa E501
        def test_word_exists(word, lst):
            return word in lst

        mocked_finder.word_exists.side_effect = test_word_exists

        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "words.txt",
                                     'symbols.txt')
        words = checker.get_array_of_words_with_swapped_symbols('word',
                                                                ['wrod', 'sd'])
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'wrod')

    def test_get_array_of_words_with_swapped_symbols_true_parameters(self):
        checker = self.checker
        words = checker.get_array_of_words_with_swapped_symbols('word',
                                                                ['wrod', 'sd'])
        self.assertEqual(len(words), 1)
        self.assertEqual(words[0], 'wrod')

    def test_get_array_of_words_with_swapped_symbols_empty_words_list(self):
        checker = self.checker
        words = checker.get_array_of_words_with_swapped_symbols('word',
                                                                [])
        self.assertEqual(words, [])

    @patch('word_check.SimilarWordsFinder')
    def test_get_similar_words_true_parameters_bl(self,
                                                  mocked_finder):
        def test_word_exists(word, lst):
            return word in lst

        mocked_finder.word_exists.side_effect = test_word_exists
        mocked_finder.get_list_of_words.return_value = []
        mocked_finder.get_array_of_words_with_extra_symbol.return_value = [
            'word/',
            'word:',
            'word,'
        ]
        mocked_finder.get_array_of_words_with_deleted_symbol.return_value = [
            'wor',
            'wod',
            'wrd'
        ]
        mocked_finder.get_array_of_words_with_replaced_symbol.return_value = [  # noqa E501
            'dwor',
            'wdor'
        ]
        mocked_finder.get_array_of_words_with_swapped_symbols.return_value = [  # noqa E501
            'dorw'
        ]

        checker = SimilarWordsFinder(self.true_url,
                                     self.true_raw_url,
                                     "words.txt",
                                     'symbols.txt')

        words = checker.get_similar_words('word')
        true_words = [
            'word/',
            'word:',
            'word,',
            'wor',
            'wod',
            'wrd',
            'dwor',
            'wdor',
            'dorw'
        ]

        for word in true_words:
            self.assertIn(word, words)

    def test_get_similar_words_true_parameters(self):
        checker = self.checker
        words = checker.get_similar_words('live')
        self.assertEqual(words, ['life'])

    def test_get_similar_words_word_in_list(self):
        checker = self.checker
        words = checker.get_similar_words('life')
        self.assertIsNone(words)

    def test_get_similar_words_empty_words_list(self):
        checker = self.checker
        words = checker.get_similar_words('live', words_filename='empty.txt')
        self.assertEqual(words, [])

    def test_get_similar_words_empty_symbols_list(self):
        checker = self.checker
        words = checker.get_similar_words('live', symbols_filename='empty.txt')
        self.assertEqual(words, [])


class TestWordCheckNegative(unittest.TestCase):
    true_url = 'https://github.com/Alxej/testing_repo/tree/main' # noqa E501
    true_raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main' # noqa E501
    checker = SimilarWordsFinder(true_url,
                                 true_raw_url,
                                 "words.txt",
                                 'symbols.txt')

    def test_initialize_with_wrong_parameters(self):
        with self.assertRaises(FileExistsError):
            SimilarWordsFinder("sdasdsad", 'symbosadas')

    def test_get_list_of_words_no_file(self):
        with self.assertRaises(FileExistsError):
            checker = self.checker
            checker.get_list_of_words("sadsadsa")

    def test_get_array_of_words_with_extra_symbol_wrong_word_type(self):
        with self.assertRaises(TypeError):
            checker = self.checker
            checker.get_array_of_words_with_extra_symbol(10, [], [])

    def test_get_array_of_words_with_replaced_symbol_wrong_word_type(self):
        with self.assertRaises(TypeError):
            checker = self.checker
            checker.get_array_of_words_with_replaced_symbol(10, [], [])

    def test_get_array_of_words_with_deleted_symbol_wrong_word_type(self):
        with self.assertRaises(TypeError):
            checker = self.checker
            checker.get_array_of_words_with_deleted_symbol(10, [])

    def test_get_array_of_words_with_swapped_symbols_wrong_word_type(self):
        with self.assertRaises(TypeError):
            checker = self.checker
            checker.get_array_of_words_with_swapped_symbols(10, [])

    def test_get_similar_words_wrong_word_type(self):
        with self.assertRaises(TypeError):
            checker = self.checker
            checker.get_similar_words(10)

    def test_get_similar_words_no_file(self):
        checker = self.checker
        with self.assertRaises(FileExistsError):
            checker.get_similar_words("word", 'sadsad', 'symbols.txt')

        with self.assertRaises(FileExistsError):
            checker.get_similar_words("word", 'words.txt', 'sadsad')


if __name__ == '__main__':
    unittest.main()