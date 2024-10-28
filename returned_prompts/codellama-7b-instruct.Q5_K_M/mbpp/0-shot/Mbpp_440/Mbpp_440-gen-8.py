def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word in ["very", "really", "actually", "also", "especially", "basically", "pretty", "very", "mostly"]:
            return i, len(word), word
    return -1, -1, ''

def find_adverb_position(sentence):
    adverbs = ['very', 'really', 'actually', 'also', 'especially', 'basically', 'pretty', 'mostly']
    for i in range(len(sentence.split())):
        if sentence.split()[i] in adverbs:
            return i, len(sentence.split()[i]), sentence.split()[i]
    return -1, -1, ''



