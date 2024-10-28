def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word[-1] == '!':
            return i, word.index('!'), word[:-1]
    return None