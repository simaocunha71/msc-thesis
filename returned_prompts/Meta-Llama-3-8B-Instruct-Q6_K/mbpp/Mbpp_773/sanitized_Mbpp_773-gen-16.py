def occurance_substring(text, substring):
    start = 0
    while start < len(text):
        pos = text.find(substring, start)
        if pos != -1:
            return substring, pos, pos + len(substring)
        start += 1
    return None