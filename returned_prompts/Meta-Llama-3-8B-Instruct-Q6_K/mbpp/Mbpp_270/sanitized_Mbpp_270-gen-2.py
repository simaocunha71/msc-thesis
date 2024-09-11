def sum_even_and_even_index(lst):
    return sum([i for i in lst if i % 2 == 0 and lst.index(i) % 2 == 0])  # O(n^2) time complexity
    # or
    return sum([i for i in lst if i % 2 == 0 and (lst.index(i) // 2) * 2 == i])  # O(n) time complexity
    # or
    result = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 == 0:
            result += num
    return result