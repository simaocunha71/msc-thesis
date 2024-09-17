def occurance_substring(s, substring):
    if substring in s:
        start = s.index(substring)
        end = start + len(substring)
        return substring, start, end
    else:
        return None