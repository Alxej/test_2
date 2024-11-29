from word_check import SimilarWordsFinder


if __name__ == '__main__':
    url = 'https://github.com/nevmenandr/word2vec-russian-novels/tree/master/books_before' # noqa E501
    raw_url = 'https://raw.githubusercontent.com/nevmenandr/word2vec-russian-novels/master/books_before' # noqa E501
    finder = SimilarWordsFinder(url, raw_url)
    print(finder.get_similar_words("просто"))