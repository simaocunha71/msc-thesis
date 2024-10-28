def find_adverb_position(sentence):
    adverb = ''
    for i, word in enumerate(sentence.split()):
        if word[-2:] == 'ly':
            adverb = word
            break
    return (i, len(adverb), adverb)