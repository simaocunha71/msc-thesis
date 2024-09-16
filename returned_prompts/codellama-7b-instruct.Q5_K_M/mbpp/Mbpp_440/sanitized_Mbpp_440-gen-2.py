def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word in ('quickly', 'quick', 'fast', 'fastest', 'soon', 'sooner', 'later', 'later', 'slowly', 'slow', 'slowest', 'eventually', 'eventually'):
            return (i, len(sentence.split()[i:]) + i, word)
    return (None, None, None)