import re
def find_adverb_position(sentence):
    adverbs = re.findall(r'\b(ly|quickly|loudly|happily|wisely|silently|slowly|carefully|gently|patiently|calmly|quietly|silently)\b', sentence.lower())
    if adverbs:
        return (0, len(sentence)-len(adverbs[0]), adverbs[0])
    else:
        return (None, None, None)