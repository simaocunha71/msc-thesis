
def find_adverb_position(sentence: str) -> tuple:
    adverbs = ['clearly', 'quickly', 'easily', 'strongly', 'openly']
    for i, word in enumerate(sentence.split()):
        if word in adverbs:
            return (i, word)
    return (None, None)


