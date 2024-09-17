def first_repeated_char(str1):
    for index, char in enumerate(str1):
        if str1.count(char) > 1:
            return char
    return "None"