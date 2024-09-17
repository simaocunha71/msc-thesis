
def first_non_repeating_character(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1:
            return char
    return None

