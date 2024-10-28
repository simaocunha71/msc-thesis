def occurance_substring(str, substring):
    start = str.find(substring)
    if start == -1:
        return None
    return substring, start, start + len(substring)