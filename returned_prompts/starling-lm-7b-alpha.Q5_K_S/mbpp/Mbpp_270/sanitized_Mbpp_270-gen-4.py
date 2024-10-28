def sum_even_and_even_index(lst):
    return sum([i for i in lst if i % 2 == 0 and lst.index(i) % 2 == 0])