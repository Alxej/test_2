# This is a sample Python script.
import requests
import urllib
import urllib3
from bs4 import BeautifulSoup as bs
import lxml
def get_names(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = response.data.decode('utf-8')
    index = data.find("\"tree\"")
    last_index = data.find("</script>", index)
    strings = data[index : last_index].split(',')
    new_strings = []
    for string in strings:
        if "name" in string:
            ind = string.rfind(":")
            if ".txt" in string:
                new_strings.append(string[ind + 2:len(string) - 1])
    return new_strings
def get_text(filename):
    url = 'https://raw.githubusercontent.com/nevmenandr/word2vec-russian-novels/master/books_before/' + filename
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = response.data.decode('utf-8')

    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dict_of_unique_symbols = {}
    dict_of_unique_words = {}
    word_count = 0
    filenames = get_names('https://github.com/nevmenandr/word2vec-russian-novels/tree/master/books_before')
    for filename in filenames:
        text = get_text(filename)
        words = text.split(" ")
        for word in words:
            word_count += 1
            new_word = word.split("\n")
            for signature in new_word:
                new_signature = signature.replace("\n", "")
                if new_signature.lower() not in dict_of_unique_words.keys():
                    dict_of_unique_words[new_signature.lower()] = 1
                else:
                    dict_of_unique_words[new_signature.lower()] += 1
        for symbol in text:
            if symbol not in dict_of_unique_symbols.keys():
                dict_of_unique_symbols[symbol] = 1
            else:
                dict_of_unique_symbols[symbol] += 1
    print(f"Сколько различных символов встречается в текстах? Ответ: {len(dict_of_unique_symbols.keys())}")
    sorted_symbols = sorted(dict_of_unique_symbols, key=dict_of_unique_symbols.get, reverse=True)
    print("Какие буквы чаще всего встречаются в словах?\nОтвет:")
    for i in range(0,10):
        print(f"{i+1}. {sorted_symbols[i]} - {dict_of_unique_symbols[sorted_symbols[i]]} раз(а)")
    str = ""
    for symbol in dict_of_unique_symbols.keys():
        if not symbol.isalpha():
            str += symbol

    print(f"Какие небуквенные символы присутствуют в текстах?\nОтвет: {str}")
    print(f"Сколько всего слов в текстах? Ответ: {word_count}")
    print(f"Сколько всего различных слов в текстах? Ответ: {len(dict_of_unique_words.keys())}")
    sorted_words = sorted(dict_of_unique_words, key=dict_of_unique_words.get, reverse=True)
    print("Какие слова чаще всего встречаются в текстах?\nОтвет:")
    for i in range(0, 10):
        print(f"{i + 1}. {sorted_words[i]} - {dict_of_unique_words[sorted_words[i]]} раз(а)")

    with open("symbols.txt",'w',encoding="utf-8") as file:
        for symbol in dict_of_unique_symbols.keys():
            file.write(f"{symbol} - {dict_of_unique_symbols[symbol]}\n")
    with open("words.txt",'w',encoding="utf-8") as file:
        for word in dict_of_unique_words.keys():
            new_word =word.replace("\n","")
            file.write(f"{new_word} - {dict_of_unique_words[word]}\n")



