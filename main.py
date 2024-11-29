from word_check import SimilarWordsFinder


if __name__ == '__main__':
    url = 'https://github.com/Alxej/testing_repo/tree/main' # noqa E501
    raw_url = 'https://raw.githubusercontent.com/Alxej/testing_repo/refs/heads/main' # noqa E501
    finder = SimilarWordsFinder(url, raw_url)
    print(finder.get_list_of_words('words.txt'))