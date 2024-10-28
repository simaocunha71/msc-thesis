def remove_Occ(string: str, char: str) -> str:
    string = string.replace(char, '', 1)
    string = string.rstrip(char)
    string = string.lstrip(char)
    return string

