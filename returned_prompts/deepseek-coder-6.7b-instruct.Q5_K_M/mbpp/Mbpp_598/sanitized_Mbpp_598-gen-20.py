def armstrong_number(num):
    num_str = str(num)
    return num == sum(int(digit) ** len(num_str) for digit in num_str)