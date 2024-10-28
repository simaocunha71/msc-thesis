
    divisible_by_three = [v for i, v in enumerate(l) if i % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = l[:]
    for i, v in enumerate(l):
        if i % 3 == 0:
            result[i] = sorted_divisible_by_three.pop(0)
    return result


print(sort_third([5, 6, 3, 4, 8, 9, 2]))


def sort_third(lst):
    l = lst[:]
    sorted_3rd_idx_values = sorted(l[i] for i in range(len(l)) if i % 3 == 0)
    for i, v in enumerate(l):
        if i % 3 == 0:
            l[i] = sorted_3rd_idx_values.pop(0)
    return l


print(sort_third([5, 6, 3, 4, 8, 9, 2]))

# Test cases
print(sort_third([1, 2, 3]))  # Expected: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected: [2, 6, 3, 4, 8, 9, 5]
print(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 6, 10, 11, 9]
print(sort_third([]))  # Expected: []

"""
The function `sort_third` takes a list `lst` as input. It first creates a copy of the list `l`. It then creates a list `sorted_3rd_idx_values` containing the values at the indices divisible by 3, sorted.