
def find_adverb_position(sentence: str) -> tuple:
    for i in range(len(sentence)):
        if sentence[i] in ["very", "so", "much", "enough", "most", "soon", "hardly", "already", "still"]:
            return i, len(sentence[i]), sentence[i]
    for i in range(len(sentence)):
        if sentence[i] in ["very", "so", "much", "enough", "most", "soon", "hardly", "already", "still"]:
            return i, len(sentence[i]), sentence[i]
    return None


