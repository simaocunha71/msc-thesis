def count_integer(lst):
    return sum(isinstance(i, int) for i in lst)  # or lst.count(i) for i in lst if isinstance(i, int) else 0