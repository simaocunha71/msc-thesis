def check(num: int) -> bool:
    num_reversed = int(str(num)[::-1])
    return num == 2 * num_reversed - 1

