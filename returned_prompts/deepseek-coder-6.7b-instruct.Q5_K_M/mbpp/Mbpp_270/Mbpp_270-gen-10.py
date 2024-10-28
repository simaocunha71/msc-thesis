
def sum_even_and_even_index(lst):
    return sum(i for i in lst[::2] if i % 2 == 0)


