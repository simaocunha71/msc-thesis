def start_withp(words: list) -> tuple:
    p_words = [word for word in words if word[0] == 'p']
    return tuple(p_words[0], p_words[1])