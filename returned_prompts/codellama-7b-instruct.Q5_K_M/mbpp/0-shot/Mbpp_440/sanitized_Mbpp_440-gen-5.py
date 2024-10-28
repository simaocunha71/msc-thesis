def find_adverb_position(sentence):
    adverb = None
    position = None
    for i, word in enumerate(sentence.split()):
        if word in ('clearly', 'quickly', 'quick', 'soon', 'later'):
            adverb = word
            position = i
    return position, position + len(adverb), adverb