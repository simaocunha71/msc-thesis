def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word in ["very", "also", "most", "especially", "clearly", "quickly", "quick", "fast", "soon", "recently", "later", "long", "longer"]:
            return i, len(word), word
    return -1, -1, ''
