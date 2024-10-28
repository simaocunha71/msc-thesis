
def sum_squares(lst):
    return sum(i**(1 if i%4 else 3) for i in lst)
