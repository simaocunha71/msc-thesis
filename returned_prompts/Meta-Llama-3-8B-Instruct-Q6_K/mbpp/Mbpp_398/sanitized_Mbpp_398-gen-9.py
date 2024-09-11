def sum_of_digits(lst):
    return sum(sum(map(int, str(x))) for x in lst)  # map converts each string to a list of digits, sum sums the digits, and the outer sum sums the sums