
def flip_case(string: str) -> str:
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char
    return new_string

