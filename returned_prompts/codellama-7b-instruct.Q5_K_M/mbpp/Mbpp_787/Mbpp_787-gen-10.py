def text_match_three(text):
    if len(text) != 4:
        return False
    if text[0] != 'a':
        return False
    count = 0
    for i in range(1, 4):
        if text[i] == 'b':
            count += 1
        else:
            return False
    return count == 3


