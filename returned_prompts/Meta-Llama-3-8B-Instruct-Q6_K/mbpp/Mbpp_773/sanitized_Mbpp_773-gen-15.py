def occurance_substring(string, substring):
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            return substring, pos, pos+len(substring)
        start += 1
    return None