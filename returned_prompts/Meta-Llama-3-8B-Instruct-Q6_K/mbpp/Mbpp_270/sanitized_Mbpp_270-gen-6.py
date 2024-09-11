def sum_even_and_even_index(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 0 and x % 2 == 0)  # Check if index is even and the number is even