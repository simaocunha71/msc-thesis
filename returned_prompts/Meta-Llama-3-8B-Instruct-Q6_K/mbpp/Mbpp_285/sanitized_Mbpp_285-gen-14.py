def text_match_two_three(text):
    for i in range(len(text) - 3):
        if text[i] == 'a' and text[i+1:i+4].count('b') in [2, 3]:
            return True
    return False