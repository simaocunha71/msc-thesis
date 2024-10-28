def occurance_substring(string, substring):
    if substring in string:
        return substring, string.index(substring), len(substring)
    return None