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

# Tests
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
assert occurance_substring('python programming, python language','language')==('language', 11, 17)
assert occurance_substring('python programming, python language','languages')==None
assert occurance_substring('python programming, python language','programming')==('programming', 0, 11)
assert occurance_substring('python programming, python language','programming,')==('programming', 0, 11)
assert occurance_substring('python programming, python language','programming')==('programming', 0, 11)
assert occurance_substring('python programming, python language','python',)==('python', 0, 6)
assert occurance_substring('python programming, python language','programming, python',)==('programming', 0, 11)
assert occurance_substring('python programming, python language','programming, python language',)==('programming', 0, 11)


