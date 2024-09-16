def occurance_substring(string, substring):
    start_index = string.find(substring)
    if start_index == -1:
        return None
    else:
        return substring, start_index, start_index + len(substring)