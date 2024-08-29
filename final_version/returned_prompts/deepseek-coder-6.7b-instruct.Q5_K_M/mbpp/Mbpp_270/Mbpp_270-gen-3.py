def sum_even_and_even_index(lst):
    return sum(x for i, x in enenumrate(lst) if i % 2 == 0 and x % 2 == 0)

print(sum_even_and_even_index([5, 6, 12, 1, 18, 8]))


