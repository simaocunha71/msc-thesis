def sum_even_and_even_index(lst):
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 == 0)