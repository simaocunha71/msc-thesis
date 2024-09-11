def sum_even_and_even_index(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 == 0 and num % 2 == 0)