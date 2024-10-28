
import re
def find_adverb_position(sent):
    adverbs = re.findall(r'\b(?:very|just|enough|too)\b', sent)
    if adverbs:
        adverb = adverbs[0]
        start = sent.find(adverb)
        end = start + len(adverb) - 1
        return (start, end, adverb)
    else:
        return None


