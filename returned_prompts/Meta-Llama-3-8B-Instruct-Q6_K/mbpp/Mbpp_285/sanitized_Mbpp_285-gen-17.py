def text_match_two_three(s):
    if len(s) < 3:
        return False
    if s[0] == 'a' and s[1] == 'b' and s[2] == 'b':
        return True
    if s[0] == 'a' and s[1] == 'b' and s[2] == 'b' and s[3] == 'b':
        return True
    return False