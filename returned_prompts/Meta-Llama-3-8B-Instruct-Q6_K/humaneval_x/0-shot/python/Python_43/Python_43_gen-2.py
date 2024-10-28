def pairs_sum_to_zero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
# test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
print(pairs_sum_to_zero([0, 0]))  # True
print(pairs_sum_to_zero([-1, 1]))  # True
print(pairs_sum_to_zero([-1, 1, 2]))  # True
print(pairs_sum_to_zero([1, -1, 2]))  # True
print(pairs_sum_to_zero([1, -1, 2, 3]))  # True
print(pairs_sum_to_zero([1, -2, 3]))  # True
print(pairs_sum_to_zero([1, -1, 0]))  # True
print(pairs_sum_to_zero([1, 0, 1]))  # True
print(pairs_sum_to_zero([-1, 1, 2, 3]))  # True
print(pairs_sum_to_zero([1, -1, 0, 1]))  # True
print(pairs_sum_to_zero([1, 2, 3, 4, 5]))  # False
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6]))  # False
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7]))  # False
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8]))  # False
print(pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # False
print(pairs_sum_to_zero([1, 2, 3,