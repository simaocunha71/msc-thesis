def first_non_repeating_character(string: str) -> str:
    for char in string:
        if string.count(char) == 1:
            return char
    return None