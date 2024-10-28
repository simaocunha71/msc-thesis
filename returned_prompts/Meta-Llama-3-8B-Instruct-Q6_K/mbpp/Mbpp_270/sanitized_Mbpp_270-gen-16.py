def sum_even_and_even_index(lst):
    sum_even = 0
    for i, num in enumerate(lst):
        if i % 2 == 0 and num % 2 == 0:
            sum_even += num
    return sum_even