def sum_even_and_even_index(lst):
    sum_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 0:
            sum_even += lst[i]
    return sum_even