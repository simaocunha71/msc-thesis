def find_adverb_position(sentence):
    words = sentence.split(' ')
    for i, word in enumerate(words):
        if word.lower() in ['quickly', 'slowly', 'suddenly', 'clearly', 'easily', 'often', 'rarely', 'usually']:
            return i, words[i], words
    return -1, '', []