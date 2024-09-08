def count_integer(lst):
    return sum(1 for i in lst if isinstance(i, int))

print(count_integer([1,2,'abc',1.2])) # 2

