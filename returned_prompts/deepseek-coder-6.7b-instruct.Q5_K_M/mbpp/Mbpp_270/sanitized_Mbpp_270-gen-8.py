def sum_even_and_even_index(lst):
    return sum(x for i, x in enenumarate(lst) if i % 2 == 0 and x % 2 == 0)