
def sum_of_digits(lst):
    return sum(sum(divmod(int(i), 10) for i in str(num)) for num in lst)

