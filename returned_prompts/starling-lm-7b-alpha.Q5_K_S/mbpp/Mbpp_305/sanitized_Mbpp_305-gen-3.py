def start_withp(words):
    p_words = [word for word in words if word.startswith('p')]
    if len(p_words) == 0:
        return None
    return p_words[0], p_words[1]