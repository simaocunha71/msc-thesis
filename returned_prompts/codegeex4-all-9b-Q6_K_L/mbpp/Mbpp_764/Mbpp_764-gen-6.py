def number_ctr(str: str) -> int:
    num = 0
    for i in str:
        if i.isdigit():
            num += 1
    return num

