
def find_Parity(num):
    num_str = str(num)
    sum_digits = sum(int(digit) for digit in num_str)
    return sum_digits % 2 != 0

print(find_Parity(12))  # False

