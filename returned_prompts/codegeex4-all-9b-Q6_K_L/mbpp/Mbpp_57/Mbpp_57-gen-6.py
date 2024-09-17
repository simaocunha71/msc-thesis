def find_Max_Num(digits: list) -> int:
    return int(''.join(map(str, sorted(digits, reverse=True))))