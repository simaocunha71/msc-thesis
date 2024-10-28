
def move_num(s: str) -> str:
    numbers = [i for i in s if i.isdigit()]
    return s.replace("".join(numbers), "") + "".join(numbers)


