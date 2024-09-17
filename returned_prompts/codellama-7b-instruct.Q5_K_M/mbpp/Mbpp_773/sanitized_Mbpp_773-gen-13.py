def occurance_substring(string: str, substring: str) -> tuple:
    if substring in string:
        return (substring, string.index(substring), string.index(substring) + len(substring))
    else:
        return None