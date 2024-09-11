import re
def find_adverb_position(sentence):
    match = re.search(r'\b(adv|ly)\b', sentence, re.IGNORECASE)
    if match:
        return (match.start(), match.end(), match.group())
    return None