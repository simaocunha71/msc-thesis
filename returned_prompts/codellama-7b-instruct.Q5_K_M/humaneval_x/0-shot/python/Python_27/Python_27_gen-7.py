

def flip_case(string: str) -> str:
    result = ''
    for c in string:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
    return result




