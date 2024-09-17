import re
def find_adverb_position(sentence: str):
    adverb = re.findall(r'\w+ly', sentence)
    if adverb:
        return (sentence.index(adverb[0]), len(adverb[0]), adverb[0])
    else:
        return None

