def occurance_substring(string,substring):
    # find the first occurrence of substring
    first_index = string.find(substring)
    # if substring not found return None
    if first_index == -1:
        return None
    # find the last occurrence of substring
    last_index = string[first_index:].find(substring)
    # if last_index == -1:
    #     last_index = len(string)-1
    # return substring, first_index, last_index
    return substring, first_index, first_index + last_index