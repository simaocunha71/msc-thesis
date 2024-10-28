def text_match_two_three(s):
    for i in range(len(s)-2):
        if s[i] == 'a' and s[i+1] == 'b' and s[i+2] == 'b':
            return True
    return False