def text_match_three(s):
    if len(s) < 4:
        return False
    if s[0] != 'a':
        return False
    if s[1:4] != 'bbB':
        return False
    return True