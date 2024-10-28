
def move_num(s: str) -> str:
    nums = [i for i in s if i.isdigit()]
    others = [i for i in s if not i.isdigit()]
    return ''.join(others + nums)


