def find_adverb_position(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if words[i] in ['clearly', 'easily', 'often', 'quickly', 'slowly', 'carefully', 'tenderly']:
            return (i, i+1, words[i])
    return None