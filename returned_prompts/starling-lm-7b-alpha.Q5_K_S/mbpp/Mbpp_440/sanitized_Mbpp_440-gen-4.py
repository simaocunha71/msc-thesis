def find_adverb_position(sentence):
    '''
    Find the first adverb and their positions in a given sentence
    '''
    adverbs = ['quickly', 'clearly', 'slowly', 'easily', 'usually']
    for i, word in enumerate(sentence.split()):
        if word.lower() in adverbs:
            return i, len(word), word
    return None