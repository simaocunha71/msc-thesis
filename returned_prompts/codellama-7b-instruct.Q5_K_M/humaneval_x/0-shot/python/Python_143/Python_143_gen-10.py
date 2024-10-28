
def words_in_sentence(sentence):
    # split sentence into list of words
    words = sentence.split()
    # filter words to keep only prime length words
    prime_words = list(filter(lambda word: len(word) % 2 == 1, words))
    # join prime words back into a string
    return ' '.join(prime_words)
