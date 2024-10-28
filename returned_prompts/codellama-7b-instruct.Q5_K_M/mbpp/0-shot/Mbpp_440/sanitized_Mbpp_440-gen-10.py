def find_adverb_position(sentence):
    adverb = ''
    adverb_position = []
    for i, word in enumerate(sentence.split()):
        if word in ['quickly', 'quick', 'soon', 'fast', 'slow', 'quickest', 'slowest']:
            adverb_position.append((i, word, adverb))
        adverb = word
    return adverb_position