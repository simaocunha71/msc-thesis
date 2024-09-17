def sum_digits(num: int) -> int:
    num_str = str(num)
    sum_num_str = 0
    for i in num_str:
        sum_num_str += int(i)
    return sum_num_str