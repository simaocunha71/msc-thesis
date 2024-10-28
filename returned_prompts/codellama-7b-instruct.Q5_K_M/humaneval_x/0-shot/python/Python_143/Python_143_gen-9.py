
def words_in_sentence(sentence):
    return ' '.join(filter(lambda x: len(x) % 2 == 1, sentence.split()))