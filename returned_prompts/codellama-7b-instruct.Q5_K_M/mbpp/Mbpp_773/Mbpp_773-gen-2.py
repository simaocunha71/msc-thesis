def occurance_substring(string, substring):
    start = string.find(substring)
    if start == -1:
        return None
    else:
        end = start + len(substring)
        return substring, start, end


