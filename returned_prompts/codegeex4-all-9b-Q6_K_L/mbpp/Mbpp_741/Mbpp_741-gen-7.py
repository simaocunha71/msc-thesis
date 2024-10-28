def all_Characters_Same(string: str) -> bool:
    for i in range(1, len(string)):
        if string[i] != string[0]:
            return False
    return True

