def move_num(s: str) -> str:
    nums = [c for c in s if c.isdigit()]
    non_nums = [c for c in s if not c.isdigit()]
    return ''.join(non_nums + nums)

