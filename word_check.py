import os.path
def get_list_of_words(filename):
    if not os.path.exists(filename):
        raise FileExistsError("Symbols file not exists")
    with open(filename,encoding="utf-8") as opened:
        list = []
        for line in opened:
            exist_word = line.split(" ")[0]
            if exist_word != "":
                list.append(exist_word)
        list.sort()
        return list
def word_exists(word,list):
    if word.lower() in list:
        return True
    return False
def get_array_of_words_with_extra_symbol(word,list_of_words,symbols):
    if type(word) is not str:
        raise TypeError("Word should be a string")
    list = []
    for symbol in symbols:
        for position in range(0,len(word) * 2, 2):
            new_word = word[:position] + symbol + word[position:]
            if word_exists(new_word,list_of_words):
                list.append(new_word.lower())
    return list
def get_array_of_words_with_replaced_symbol(word,list_of_words,symbols):
    if type(word) is not str:
        raise TypeError("Word should be a string")
    list = []
    for symbol in symbols:
        for position in range(0, len(word)):
            new_word = word[:position] + symbol + word[position + 1:]
            if word_exists(new_word,list_of_words):
                list.append(new_word.lower())
    return list
def get_array_of_words_with_deleted_symbol(word,list_of_words):
    if type(word) is not str:
        raise TypeError("Word should be a string")
    list= []
    for position in range(0,len(word)):
        new_word = ''.join([word[i] for i in range(len(word)) if i != position])
        if word_exists(new_word,list_of_words):
            list.append(new_word.lower())
    return list
def get_array_of_words_with_swapped_symbols(word,list_of_words):
    if type(word) is not str:
        raise TypeError("Word should be a string")
    mylist= []
    for position in range(0,len(word)-1):
        new_word = word
        list1 = list(new_word)
        char = list1[position]
        list1[position] = list1[position+1]
        list1[position+1] = char
        new_word = ''.join(list1)
        if word_exists(new_word,list_of_words):
            mylist.append(new_word.lower())
    return mylist
def get_array_of_similar_words(word, words_filename, symbols_filename):
    if type(word) is not str:
        raise TypeError("Word should be a string")
    if not os.path.exists(words_filename):
        raise FileExistsError("Word file not exists")
    if not os.path.exists(symbols_filename):
        raise FileExistsError("Symbols file not exists")
    new_word = word.split(" ")[0]
    result= {}
    list_of_words = get_list_of_words(words_filename)
    list_of_symbols = get_list_of_words(symbols_filename)
    if word_exists(new_word, list_of_words):
        return None
    list1 = get_array_of_words_with_extra_symbol(new_word,list_of_words,list_of_symbols)
    list2 = get_array_of_words_with_deleted_symbol(new_word,list_of_words)
    list3 = get_array_of_words_with_replaced_symbol(new_word,list_of_words,list_of_symbols)
    list4 = get_array_of_words_with_swapped_symbols(new_word,list_of_words)
    for word in list1+list2+list3+list4:
        if word not in result.keys():
            result[word] = 1
        else:
            result[word] += 1
    return result.keys()
if __name__ == '__main__':
    list_of_words = get_list_of_words("words.txt")
    print("Введите слово:")
    word = input().split(" ")[0]
    if not word_exists(word,list_of_words):
        result = get_array_of_similar_words(word,"words.txt", "symbols.txt")
        if len(result) > 0 :
            print(f"Слова, похожие на введённое:")
            for word in result:
                print(word)
        else:
            print("Похожих слов не найдено")
    else:
        print(f"Слово \"{word}\" находится в словаре")