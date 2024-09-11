def text_match_two_three(text: str) -> bool:
    if len(text) < 3:
        return False
    if text[0] != 'a':
        return False
    if len(text[1:]) < 2:
        return False
    if text[1] != 'b':
        return False
    if len(text[1:]) >= 3 and text[2] != 'b':
        return False
    if len(text[1:]) >= 3 and text[2] == 'b':
        if len(text[1:]) >= 4 and text[3] != 'b':
            return False
    return True