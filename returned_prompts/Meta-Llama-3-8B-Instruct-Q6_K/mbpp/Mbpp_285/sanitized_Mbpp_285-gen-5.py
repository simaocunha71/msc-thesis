def text_match_two_three(s):
    for i in range(len(s)-3):
        if s[i] == 'a' and s[i+1:i+4].count('b') in [2,3]:
            return True
    return False