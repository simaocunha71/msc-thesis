
def first_non_repeating_character(str1):
    count = {}
    for i in str1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key, value in count.items():
        if value == 1:
            return key
    return None


