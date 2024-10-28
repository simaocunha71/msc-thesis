import re
def find_adverb_position(sentence):
    pattern = r'\b(adverb)\b'
    matches = re.finditer(pattern, sentence)
    for match in matches:
        return match.start(), match.end(), match.group(0)