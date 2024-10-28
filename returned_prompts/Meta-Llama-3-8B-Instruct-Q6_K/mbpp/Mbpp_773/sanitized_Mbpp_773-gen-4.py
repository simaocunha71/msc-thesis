def occurance_substring(s, substring):
    if substring not in s:
        return None
    return substring, s.index(substring), s.index(substring) + len(substring) - 1