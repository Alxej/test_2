import urllib3


class WordsParser:

    def get_names(self, url):
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', url)
        except Exception:
            raise ValueError
        if response.status != 200:
            raise ValueError
        data = response.data.decode('utf-8')
        index = data.find("\"tree\"")
        last_index = data.find("</script>", index)
        strings = data[index: last_index].split(',')
        new_strings = []
        for string in strings:
            if "name" in string:
                ind = string.rfind(":")
                if ".txt" in string:
                    new_strings.append(string[ind + 2:len(string) - 1])
        print(new_strings)
        return new_strings

    def get_text(self, filename, url):
        new_url = url + '/' + filename
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', new_url)
        except Exception:
            raise ValueError
        if response.status != 200:
            raise ValueError
        data = response.data.decode('utf-8')

        return data

    def write_file(self, filename, data_dict, remove_n=True):
        with open(filename, 'w', encoding="utf-8") as f:
            for key in data_dict.keys():
                new_key = key
                if remove_n:
                    new_key = key.replace("\n", "")
                f.write(f"{new_key} - {data_dict[key]}\n")

    def save_words_and_symbols(self,
                               dict_of_unique_symbols,
                               dict_of_unique_words,
                               symbols_filename="symbols.txt",
                               words_filename="words.txt"):
        self.write_file(symbols_filename,
                        dict_of_unique_symbols,
                        False)
        self.write_file(words_filename, dict_of_unique_words)

    def get_unique_words_and_symbols(self, texts_folder_url, raw_url):
        dict_of_unique_symbols = {}
        dict_of_unique_words = {}
        word_count = 0
        filenames = self.get_names(texts_folder_url)
        for filename in filenames:
            text = self.get_text(filename, raw_url)
            words = text.split(" ")
            for word in words:
                word_count += 1
                new_word = word.split("\n")
                for signature in new_word:
                    new_signature = signature.replace("\n", "")
                    if new_signature.lower() not in dict_of_unique_words.keys(): # noqa E501
                        dict_of_unique_words[new_signature.lower()] = 1
                    else:
                        dict_of_unique_words[new_signature.lower()] += 1
            for symbol in text:
                if symbol not in dict_of_unique_symbols.keys():
                    dict_of_unique_symbols[symbol] = 1
                else:
                    dict_of_unique_symbols[symbol] += 1

        return {'words': dict_of_unique_words,
                'symbols': dict_of_unique_symbols}

    def parse_and_save(self,
                       repo_url,
                       raw_url,
                       words_path="words.txt",
                       symbol_path="symbols.txt"):
        unique_words_and_symbols = self.get_unique_words_and_symbols(repo_url, raw_url) # noqa E501
        words = unique_words_and_symbols['words']
        symbols = unique_words_and_symbols['symbols']
        self.save_words_and_symbols(symbols,
                                    words,
                                    symbol_path,
                                    words_path)
