
def remove_dirty_chars(str1: str, str2: str) -> str:
    for char in str2:
        str1 = str1.replace(char, "")
    return str1


