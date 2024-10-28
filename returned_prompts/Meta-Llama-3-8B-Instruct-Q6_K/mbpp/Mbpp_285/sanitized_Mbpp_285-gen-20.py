def text_match_two_three(s):
    if len(s) < 3:
        return False
    if s[0] != 'a':
        return False
    if s[1] != 'b':
        return False
    if s[2] != 'b':
        return False
    return True