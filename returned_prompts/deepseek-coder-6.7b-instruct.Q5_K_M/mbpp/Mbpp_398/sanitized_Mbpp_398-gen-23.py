def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)