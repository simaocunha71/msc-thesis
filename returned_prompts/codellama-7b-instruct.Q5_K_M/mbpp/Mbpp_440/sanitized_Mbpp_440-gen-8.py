def find_adverb_position(sentence):
    for i, word in enumerate(sentence.split()):
        if word in ["very", "really", "actually", "also", "especially", "basically", "pretty", "very", "mostly"]:
            return i, len(word), word
    return -1, -1, ''