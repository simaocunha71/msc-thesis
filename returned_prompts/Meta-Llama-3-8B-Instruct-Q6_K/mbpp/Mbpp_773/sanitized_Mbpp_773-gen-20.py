def occurance_substring(big_string, substring):
    try:
        index = big_string.index(substring)
        return substring, index, index + len(substring)
    except ValueError:
        return None