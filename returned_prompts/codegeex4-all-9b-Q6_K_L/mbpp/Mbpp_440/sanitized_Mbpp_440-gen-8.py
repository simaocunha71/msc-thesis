def find_adverb_position(sentence):
    import re
    adverb = re.findall(r'\w+ly', sentence)
    if adverb:
        return (sentence.index(adverb[0]), sentence.index(adverb[0]) + len(adverb[0]) - 1, adverb[0])
    else:
        return None