import re
def find_adverb_position(sentence):
    adverbs = ['quickly', 'slowly', 'loudly', 'silently', 'clearly']
    for i, word in enumerate(re.findall(r'\b\w+\b', sentence.lower())):
        if word in adverbs:
            return (i, i+len(word), word)
    return None