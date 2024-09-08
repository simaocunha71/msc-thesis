def occurance_substring(string, substring):
    index = string.find(substring)
    if index == -1:
        return None
    return (substring, index, index + len(substring))