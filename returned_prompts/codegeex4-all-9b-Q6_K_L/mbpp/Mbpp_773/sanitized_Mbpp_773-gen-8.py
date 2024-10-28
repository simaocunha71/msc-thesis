def occurance_substring(string, substring):
    if substring not in string:
        return None
    else:
        position = string.index(substring)
        return (substring, position, position + len(substring) - 1)