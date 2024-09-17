def text_match_two_three(s):
    s = s.lower()
    if "a" in s and "b" in s:
        if s.count("b")>=2:
            return True
    return False