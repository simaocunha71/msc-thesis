def find_adverb_position(sentence):
    import re
    adverb_pattern = r'\b(?:clearly|obviously|absolutely)\b'
    match = re.search(adverb_pattern, sentence)
    if match:
        return (match.start(), match.end(), match.group(0))
    else:
        return None