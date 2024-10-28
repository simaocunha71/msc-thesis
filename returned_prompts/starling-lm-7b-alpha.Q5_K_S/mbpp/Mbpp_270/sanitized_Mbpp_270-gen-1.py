def sum_even_and_even_index(lst):
    total = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 == 0:
            total += num
    return total