def sum_of_digits(lst):
    return sum(sum(int(i) for i in str(x)) for x in lst)  # or return sum(sum(int(digit) for digit in str(x)) for x in lst)