def count_integer(lst):
    return sum(isinstance(i, int) for i in lst)

assert count_integer([1,2,'abc',1.2]) == 2


"""
