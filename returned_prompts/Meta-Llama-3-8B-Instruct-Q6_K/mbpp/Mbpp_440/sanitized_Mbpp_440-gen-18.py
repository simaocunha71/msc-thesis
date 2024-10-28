import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(rapidly|quickly|loudly|silently|clearly|gently|firmly|slowly|wisely|carefully|strongly|vigorously)\b', sentence, re.IGNORECASE)
    if adverbs:
        return (0, len(sentence.split()[0].encode('utf-8')) + len(adverbs[0]), adverbs[0])
    else:
        return None