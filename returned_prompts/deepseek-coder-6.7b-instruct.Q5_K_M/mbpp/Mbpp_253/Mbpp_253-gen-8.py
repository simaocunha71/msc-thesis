def count_integer(lst):
    return len([i for i in lst if isinstance(i, int)])

print(count_integer([1,2,'abc',1.2]))  # Expected output: 2

