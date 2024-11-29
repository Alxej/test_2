import os.path
from words_parser import WordsParser


class SimilarWordsFinder:
    words_filename = "words.txt"
    symbols_filename = "symbols.txt"

    def __init__(self,
                 repo_url=None,
                 raw_repo_url=None,
                 words_path="words.txt",
                 symbol_path="symbols.txt"):
        if repo_url is not None:
            parser = WordsParser()
            parser.parse_and_save(repo_url,
                                  raw_repo_url,
                                  words_path,
                                  symbol_path)
        if repo_url is None and (not os.path.exists(words_path) or not os.path.exists(symbol_path)): # noqa E501
            raise FileExistsError("No needed words or symbol file")
        self.words_filename = words_path
        self.symbols_filename = symbol_path

    def get_list_of_words(self, filename=words_filename):
        if not os.path.exists(filename):
            raise FileExistsError("Symbols file not exists")
        with open(filename, encoding="utf-8") as opened:
            lst = []
            for line in opened:
                exist_word = line.split(" ")[0]
                if exist_word != "":
                    lst.append(exist_word)
            lst.sort()
            return lst

    def word_exists(self, word, lst: list):
        return word.lower() in lst

    def get_array_of_words_with_extra_symbol(self,
                                             word,
                                             list_of_words,
                                             symbols):
        if type(word) is not str:
            raise TypeError("Word should be a string")
        lst = []
        for symbol in symbols:
            for position in range(0, len(word)):
                new_word = word[:position] + symbol + word[position:]
                if self.word_exists(new_word, list_of_words):
                    lst.append(new_word.lower())
        return lst

    def get_array_of_words_with_replaced_symbol(self,
                                                word,
                                                list_of_words,
                                                symbols):
        if type(word) is not str:
            raise TypeError("Word should be a string")
        lst = []
        for symbol in symbols:
            for position in range(0, len(word)):
                new_word = word[:position] + symbol + word[position + 1:]
                print(new_word)
                if self.word_exists(new_word, list_of_words):
                    lst.append(new_word.lower())
        return lst

    def get_array_of_words_with_deleted_symbol(self, word, list_of_words):
        if type(word) is not str:
            raise TypeError("Word should be a string")
        lst = []
        for position in range(0, len(word)):
            new_word = ''.join([word[i] for i in range(len(word)) if i != position]) # noqa E501
            if self.word_exists(new_word, list_of_words):
                lst.append(new_word.lower())
        return lst

    def get_array_of_words_with_swapped_symbols(self, word, list_of_words):
        if type(word) is not str:
            raise TypeError("Word should be a string")
        mylist = []
        for position in range(0, len(word)-1):
            new_word = word
            list1 = list(new_word)
            char = list1[position]
            list1[position] = list1[position+1]
            list1[position+1] = char
            new_word = ''.join(list1)
            if self.word_exists(new_word, list_of_words):
                mylist.append(new_word.lower())
        return mylist

    def get_similar_words(self,
                          word,
                          words_filename=words_filename,
                          symbols_filename=symbols_filename):
        if type(word) is not str:
            raise TypeError("Word should be a string")
        if not os.path.exists(words_filename):
            raise FileExistsError("Word file not exists")
        if not os.path.exists(symbols_filename):
            raise FileExistsError("Symbols file not exists")
        new_word = word.split(" ")[0]
        result = {}
        list_of_words = self.get_list_of_words(words_filename)
        list_of_symbols = self.get_list_of_words(symbols_filename)
        if self.word_exists(new_word, list_of_words):
            return None
        list1 = self.get_array_of_words_with_extra_symbol(new_word,
                                                          list_of_words,
                                                          list_of_symbols)
        list2 = self.get_array_of_words_with_deleted_symbol(new_word,
                                                            list_of_words)
        list3 = self.get_array_of_words_with_replaced_symbol(new_word,
                                                             list_of_words,
                                                             list_of_symbols)
        list4 = self.get_array_of_words_with_swapped_symbols(new_word,
                                                             list_of_words)
        for word in list1 + list2 + list3 + list4:
            if word not in result.keys():
                result[word] = 1
            else:
                result[word] += 1
        return list(result.keys())
