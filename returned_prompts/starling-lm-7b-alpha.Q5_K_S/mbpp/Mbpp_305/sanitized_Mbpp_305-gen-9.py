from collections import OrderedDict
def start_withp(words):
    p_words = [word for word in words if word.startswith('p')]
    if len(p_words) < 2:
        raise ValueError("Less than 2 words start with 'p'")
    return p_words[0], p_words[1]