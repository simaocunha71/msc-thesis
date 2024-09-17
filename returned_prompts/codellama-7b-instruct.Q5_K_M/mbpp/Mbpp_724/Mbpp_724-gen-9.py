
def power_base_sum(base, power):
    sum_of_digits = 0
    for digit in str(base**power):
        sum_of_digits += int(digit)
    return sum_of_digits


