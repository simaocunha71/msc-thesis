
def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word.endswith('ly'):
            return i, len(word), word.replace('ly', '')
    return -1, -1, None


