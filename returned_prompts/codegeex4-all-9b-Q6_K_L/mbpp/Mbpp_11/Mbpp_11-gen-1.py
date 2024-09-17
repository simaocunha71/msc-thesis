def remove_Occ(string: str, char: str) -> str:
    return string.replace(char, '', 1).rstrip(char).lstrip(char)


