import re
def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'silently', 'happily', 'unhappily', 'honestly', 'clearly', 'wisely', 'foolishly']
    pattern = r'\b(' + '|'.join(adverbs) + r')\b'
    match = re.search(pattern, sentence.lower())
    if match:
        return (match.start(), match.end(), match.group())
    return None