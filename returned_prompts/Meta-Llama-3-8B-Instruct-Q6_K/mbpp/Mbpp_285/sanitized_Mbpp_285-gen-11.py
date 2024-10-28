def text_match_two_three(s):
    if 'a' in s and 'b' in s:
        index_a = s.index('a')
        if s[index_a+1:index_a+4].count('b') in [2, 3]:
            return True
    return False