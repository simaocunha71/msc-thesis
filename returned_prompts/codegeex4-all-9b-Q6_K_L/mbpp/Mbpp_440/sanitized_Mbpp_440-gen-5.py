def find_adverb_position(sentence):
    adverb_list = ['clearly', 'quickly', 'easily', 'obviously', 'hardly', 'luckily', 'seriously', 'naturally', 'frankly', 'truthfully']
    for i, word in enumerate(sentence.split()):
        if word in adverb_list:
            return (i, len(word), word)
    return None