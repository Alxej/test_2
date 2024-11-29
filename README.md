# Тесты
## Нахождение похожих слов среди текстовых файлов репозитория
### Позитивные тесты:

### Функция: get_names(url: str)  
 - Возвращает массив названий текстовых файлов репозитория.  
 - Аргументы: url - ссылка на репозиторий
   
#### Блочные тесты:  
1. Тест ```test_get_names_true_url``` (Тест функции для существующего репозитория)  
  - Входные данные: url = 'https://github.com/nevmenandr/word2vec-russian-novels/tree/master/books_before'
  - Ожидаемый результат: ['CrimeAndPunishment.txt', 'CrimeAndPunishment_JOF.txt', 'EugeneOnegin.txt', 'EugeneOnegin_JOF.txt', 'FathersAndSons.txt', 'FathersAndSons_JOF.txt', 'MasterAndMargarita.txt', 'MasterAndMargarita_JOF.txt', 'WarAndPeace.txt', 'WarAndPeace_JOF.txt']

#### Негативные тесты:
1. Тест ```test_get_names_wrong_url``` (Тест функции c неверной ссылкой на репозиторий) 
- Входные данные: url = 'sdsadsadasd'
- Ожидаемый результат: ValueError

### Функция: get_text(filename: str, url: str) 
- Получает текст выбранного файла в репозитории.  
- Аргументы: filename - название файла, url - ссылка на репозиторий  
    
#### Блочные тесты:
Без использования внешних функций.
1. Тест ```test_get_text_true_url``` (Блочный тест получения файла с верной ссылкой)  
  - Входные данные: url = 'https://raw.githubusercontent.com/Alxej/testing/refs/heads/main', filename = 'README.md'
  - Ожидаемый результат: text = 'Лабораторная работа номер 1...\n'

#### Негативные тесты:
1. Тест ```test_get_text_wrong_url``` (Тест функции c неверной ссылкой на репозиторий) 
- Входные данные: url = 'sdsadsadasd', filename = ""sdadsd""
- Ожидаемый результат: ValueError

### Функция: write_file(filename: str, dictionary: dict, remove_n=True)
- Функция, записывающая в файл уникальные слова из репозитория и их частоту использования.  
- Аргументы: filename - название файла, куда записывается результат, dictionary - словарь со словами и частотами, remove_n - флаг для удаления переводов строк из слов
#### Блочные тесты:
1. Тест ```test_write_file_true_parameters``` (Тест с полностью корректными параметрами)
  - Входные данные: filename = "test_file.txt", dictionary = {"data": 1}
  - Ожидаемый результат: содержимое файла: data - 1

2. Тест ```test_write_file_empty_data``` (Тест с проверкой функции записи с пустым словарем)
  - Входные данные: filename = "test_file.txt", dictionary = {} 
  - Ожидаемый результат: файл создан, но пуст

3. Тест ```test_write_file_remove_n_false``` (Тест с проверкой функции записи с измененным флагом удаления переводов строк)
  - Входные данные: filename = "test_file.txt", dictionary = {"data\n": 1}
  - Ожидаемый результат: содержимое файла: data\n -  1

### Функция: save_words_and_symbols(dict_of_unique_symbols: dict, dict_of_unique_words: dict, symbols_filename = "symbols.txt", words_filename = "words.txt")
- Записывает частоты встречаемых слов и символов в тестовые файлы.
- Аргументы: dict_of_unique_symbols - словарь уникальных символов и их частот, dict_of_unique_words - словарь уникальных слов и их частот, symbols_filename - название файла для символов, words_filename- название файла для слов

#### Интеграционные тесты:
Данная функция также использует функцию write_file.
1. Тест ```test_save_words_and_symbols_true_parameters``` (Тест с записью словарей с верными параметрами и использованием реализованной функции write_file)
  - Входные данные: symbols_filename = "test_symbols.txt", words_filename = "test_words.txt",  symbols = {'a': 5}, words = {'awda\n': 10}
  - Ожидаемый результат: содержимое файла "test_symbols.txt": a - 5 , содержимое файла "test_words.txt": awda - 10

#### Блочные тесты:
Без использования внешних функций.
1. Тест ```test_save_words_and_symbols_true_parameters_block``` (Тест с записью словарей с верными параметрами без использования внешней функции write_file)
  - Входные данные: symbols_filename = "test_symbols.txt", words_filename = "test_words.txt",  symbols = {'a': 5}, words = {'awda\n': 10}
  - Ожидаемый результат: содержимое файла "test_symbols.txt": a - 5 , содержимое файла "test_words.txt": awda - 10

#### Негативные тесты:
1. Тест ```test_save_words_and_symbols_wrong_url``` (Тест функции c неверной ссылкой на репозиторий) 
- Входные данные: words = {}, symbols = {}, url = 'sdsadsadasd', filename = ""sdadsd""
- Ожидаемый результат: ValueError

### Функция: get_unique_words_and_symbols(repo_url, raw_url) 
- Считает частоту использования каждого уникального слова и символа в репозитории.
- Аргументы: repo_url - ссылка на репозиторий, raw_url - ссылка для получения содержимого файлов.
- Возвращает словарь: {'words': {}, 'symbols': {}}

#### Интеграционные тесты:
Данная функция также использует функции get_names, get_text.
1. Тест ```test_get_unique_words_and_symbols_true_parameters``` (Тест с полным вычислением с использованием реализованных функций)
  - Входные данные: repo_url = 'https://github.com/Alxej/testing_repo/tree/main', raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main'
  - Ожидаемый результат: {'words': {'#':1, 'just':1, 'life':1}, 'symbols': {'#':1, 'j': 1, 'u':1, 's': 1, 't': 1, ' ': 2, 'l': 1, 'i':1, 'f': 1, 'e': 1}}

#### Блочные тесты:
1. Тест ```test_get_unique_words_and_symbols_true_parameters_block``` (Тест с полным вычислением без использования реализованных функций)
   - Входные данные:  содержимое файлов: 'just'
   - Ожидаемый результат: {'words': {'just':1}, 'symbols': {'j': 1, 'u':1, 's': 1, 't': 1}}

2. Тест ```test_get_unique_words_and_symbols_empty_repository``` (Тест с полным вычислением без использования реализованных функций с пустым репозиторием)
   - Входные данные:  url = 'https://github.com/Alxej/t', raw_url = 'https://raw.githubusercontent.com/Alxej/t/refs/heads/main/'
   - Ожидаемый результат: {'words': {}, 'symbols': {}}

#### Негативные тесты:
1. Тест ```test_get_unique_words_and_symbols_wrong_url``` (Тест функции c неверной ссылкой на репозиторий) 
- Входные данные: url = 'sdsadsadasd', filename = ""sdadsd""
- Ожидаемый результат: ValueError

### Функция: parse_and_save(repo_url, raw_url, words_path="words.txt", symbol_path="symbols.txt")
- Считает частоту использования каждого уникального слова и символа в репозитории и записывает словари в файлы.
- Аргументы: repo_url - ссылка на репозиторий, raw_url - ссылка для получения содержимого файлов, words_path - путь для сохранения словаря с частотой слов, symbols_path - путь для сохранения словаря с частотой символов.
- Сохраняет файлы words_path и symbols_path

#### Интеграционные тесты:
Функция также использует внешние функции save_words_and_symbols и get_unique_words_and_symbols
1. Тест ```test_parse_and_save_true_parameters``` (Тест с верным форматом аргументов функции)
   - Входные данные:  url = 'https://github.com/Alxej/testing_repo/tree/main', raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main'
   - Ожидаемый результат: содержимое файла с словами: "'#' - 1\n 'just' - 1\n, 'life' - 1\n", содержимое файла с символами: "'#' - 1\n 'j' - 1\n 'u' - 1\n 's' - 1\n 't' - 1\n ' ' - 2\n 'l':  - 1\n 'i' - 1\n'f' - 1\n 'e' - 1\n"

#### Блочные тесты:
Без использования внешних функций
1. Тест ```test_parse_and_save_true_parameters``` (Тест с верным форматом аргументов функции)
   - Входные данные:  url = 'https://github.com/Alxej/testing_repo/tree/main', raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main'
   - Ожидаемый результат: содержимое файла с словами: "'#' - 1\n 'just' - 1\n, 'life' - 1\n", содержимое файла с символами: "'#' - 1\n 'j' - 1\n 'u' - 1\n 's' - 1\n 't' - 1\n ' ' - 2\n 'l':  - 1\n 'i' - 1\n'f' - 1\n 'e' - 1\n"
2 Тест ```test_parse_and_save_empty_repository```(Тест с верным форматом аргументов функции и пустым репозиторием)
 - Входные данные: ссылка на пустой репозиторий
 - Ожидаемый результат: содержимое файла с словами: "", содержимое файла с символами: ""

### Функция: __init__ класса SimilarWordsFinder(repo_url=None, raw_repo_url=None, words_path="words.txt", symbol_path="symbols.txt")
- Инициализирует поля класса и считывает необходмые частоты слов и символов в случае необходимости .
- Аргументы: repo_url - ссылка на репозиторий, raw_repo_url - ссылка на содержимые файлов, words_path - путь к файлу с сохраненными частотами слов, symbol_path - путь к файлу с сохраненными частотами символов.

#### Блочные тесты:
1. Тест ```test_initialize_with_true_parameters```(Тест инициализации с верными параметрами)
 - Входные данные: repo_url = 'https://github.com/Alxej/testing_repo/tree/main', raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main', words_path = "1.txt", symbols_path = '2.txt'
 - Ожидаемый результат: поле класса words_filename = '1.txt', symbols_path = '2.txt',  создается файл с частотами слов из репозитория, создается файл с частотами символов из репозитория

#### Негативные тесты:
1. Тест ```test_initialize_with_wrong_parameters```(Тест для инициализации с неверной ссылкой на репозиторий)
 - Входные данные: repo_url = sdasdsad, raw_url = 'symbosadas'
 - Ожидаемый результат: ValueError

### Функция: get_list_of_words(filename: str)
- Получает список слов из файла.
- Аргументы: filename - мназвание файла.
- Возвращает список слов из файла.

#### Блочные тесты:
1. Тест ```test_get_list_of_words_true_parameters```(Тест с верными параметрами)
   - Входные данные: filename = 'words.txt'
   - Выходные данные: ['#', 'just', 'life']

2. Тест ```test_get_list_of_words_empty_file```(Тест с пустым файлом)
   - Входные данные: filename = 'empty.txt'
   - Выходные данные: []  

### Функция: word_exist(word, lst)
- Проверяет наличия слова в списке.
- Аргументы: word - слов, lst - список слов.
- Возвращает булевое значение подтверждающее наличие или отсутствие файла в списке.

#### Блочные тесты:
1. Тест ```test_word_exists_true```(Тест с существующим словом)
   - Входные данные: word = 's', lst = ['s', 'ss']
   - Выходные данные: True

2. Тест ```test_word_exists_false```(Тест с несуществующим словом)
   - Входные данные: word = 'sdasdsa', lst = ['s', 'ss']
   - Выходные данные: False

#### Негативные тесты:
1. Тест ```test_get_list_of_words_no_file``` (Тест с путем к несуществующему файлу)
   - Входные данные: filename = 'sdadsadas'
   - Результат: FileExistsError
  
### Функция: get_array_of_words_with_extra_symbol(word, list_of_words, symbols)
- Находит слова в массиве, которые отличаются от введенного на 1 симол из словаря.
- Аргументы: word - слово, list_of_words - список слов, symbols - список доступных символов.
- Возвращает список слов, отличающихся от заданного на 1 символ из словаря.

#### Интеграционные тесты:
Использует функцию word_exists
1. Тест ```test_get_array_of_words_with_extra_symbol_true_parameters```(Тест с верными параметрами)
   - Входные данные: word = 'wod', list_of_words = ['word', 'sdas'], symbols = ['r', 's']
   - Выходные данные: ['word']
2. Тест ```test_get_array_of_words_with_extra_symbol_empty_word_list```(Тест с пустым массивом слов)
   - Входные данные: word = 'wod', list_of_words = [], symbols = ['r', 's']
   - Выходные данные: []
3. Тест ```test_get_array_of_words_with_extra_symbol_empty_symbol_list```(Тест с пустым массивом символов)
   - Входные данные: word = 'wod', list_of_words = ['word', 'sdas'], symbols = []
   - Выходные данные: []

#### Блочные тесты
Без использования внешних функций
1. Тест ```test_get_array_of_words_with_extra_symbol_true_parameters_block``` (Тест с верными параметрами)
   - Входные данные: word = 'wod', list_of_words = ['word', 'sdas'], symbols = ['r', 's']
   - Выходные данные: ['word']

#### Негативные тесты
1. Тест ```test_get_array_of_words_with_extra_symbol_wrong_word_type``` (Тест с неверным типом входных данных)
   - Входные данные: word = 10, list_of_words = ['word', 'sdas'], symbols = ['r', 's']
   - Выходные данные: ValueError

### Функция: get_array_of_words_with_replaces_symbol(word, list_of_words, symbols)
- Находит слова в списке, которые отличаются от введенного на 1 замененный символ.
- Аргументы: word - слово, list_of_words - список слов, symbols - список доступных символов.
- Возвращает список слов, отличающихся от заданного на 1 замененный символ из словаря.

#### Интеграционные тесты:
Использует функцию word_exists
1. Тест ```test_get_array_of_words_with_replaced_symbol_true_parameters```(Тест с верными параметрами)
   - Входные данные: word = 'word', list_of_words = ['wosd', 'sdas'], symbols = ['k', 's', 'd']
   - Выходные данные: ['word']
2. Тест ```test_get_array_of_words_with_replaced_symbol_empty_word_list```(Тест с пустым массивом слов)
   - Входные данные: word = 'word', list_of_words = [], symbols = ['k', 's', 'd']
   - Выходные данные: []
3. Тест ```test_get_array_of_words_with_replaced_symbol_empty_symbol_list```(Тест с пустым массивом символов)
   - Входные данные: word = 'word', list_of_words = ['wosd', 'sdas'], symbols = []
   - Выходные данные: []

#### Блочные тесты
Без использования внешних функций
1. Тест ```test_get_array_of_words_with_replaced_symbol_true_parameters_block``` (Тест с верными параметрами)
   - Входные данные: word = 'word', list_of_words = ['wosd', 'sdas'], symbols = ['k', 's', 'd']
   - Выходные данные: ['word']

#### Негативные тесты
1. Тест ```test_get_array_of_words_with_replaced_symbol_wrong_word_type``` (Тест с неверным типом входных данных)
   - Входные данные: word = 10, list_of_words = ['wosd', 'sdas'], symbols = ['k', 's', 'd']
   - Выходные данные: ValueError

### Функция: get_array_of_words_with_deleted_symbol(word, list_of_words)
- Находит слова в списке, которые отличаются от введенного на 1 удаленный символ.
- Аргументы: word - слово, list_of_words - список слов.
- Возвращает список слов, отличающихся от заданного на 1 замененный символ из словаря.

#### Интеграционные тесты:
Использует функцию word_exists
1. Тест ```test_get_array_of_words_with_deleted_symbol_true_parameters```(Тест с верными параметрами)
   - Входные данные: word = 'wordk', list_of_words = ['word', 'sdas']
   - Выходные данные: ['word']
2. Тест ```test_get_array_of_words_with_deleted_symbol_empty_word_list```(Тест с пустым массивом слов)
   - Входные данные: word = 'wordk', list_of_words = []
   - Выходные данные: []

#### Блочные тесты
Без использования внешних функций
1. Тест ```test_get_array_of_words_with_deleted_symbol_true_parameters_block``` (Тест с верными параметрами)
   - Входные данные: word = 'wordk', list_of_words = ['word', 'sdas']
   - Выходные данные: ['word']

#### Негативные тесты
1. Тест ```test_get_array_of_words_with_deleted_symbol_wrong_word_type``` (Тест с неверным типом входных данных)
   - Входные данные: word = 10, list_of_words = ['word', 'sdas']
   - Выходные данные: ValueError
  
### Функция: get_array_of_words_with_swapped_symbols(word, list_of_words)
- Находит слова в списке, которые отличаются от введенного на 2 символами, поменянными местами.
- Аргументы: word - слово, list_of_words - список слов.
- Возвращает список слов, отличающихся от заданного на поменянных местами символа.

#### Интеграционные тесты:
Использует функцию word_exists
1. Тест ```test_get_array_of_words_with_swapped_symbols_true_parameters```(Тест с верными параметрами)
   - Входные данные: word = 'word', list_of_words = ['wrod', 'sd']
   - Выходные данные: ['wrod']
2. Тест ```test_get_array_of_words_with_swapped_symbols_empty_word_list```(Тест с пустым массивом слов)
   - Входные данные: word = 'wordk', list_of_words = []
   - Выходные данные: []

#### Блочные тесты
Без использования внешних функций
1. Тест ```test_get_array_of_words_with_swapped_symbols_true_parameters_block``` (Тест с верными параметрами)
   - Входные данные: word = 'word', list_of_words = ['wrod', 'sd']
   - Выходные данные: ['wrod']

#### Негативные тесты
1. Тест ```test_get_array_of_words_with_swapped_symbols_wrong_word_type``` (Тест с неверным типом входных данных)
   - Входные данные: word = 10, list_of_words = ['word', 'sdas']
   - Выходные данные: ValueError

## Аттестационные тесты
1. Тест 1 - проверка запуска программы
 - Действия: пользователь запускает программу
 - Ожидаемый результат: программа запрашивает слово для поиска
