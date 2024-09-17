
def sum_of_squares_except_min(lst):
    lst.remove(min(lst))
    return sum(i**