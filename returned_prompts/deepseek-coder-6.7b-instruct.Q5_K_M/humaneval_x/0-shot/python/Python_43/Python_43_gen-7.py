
    l.sort()
    left = 0
    right = len(l) - 1
    while left < right:
        sum = l[left] + l[right]
        if sum > 0:
            right -= 1
        elif sum < 0:
            left += 1
        else:
            return True
    return False


print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1]))  # False
print(pairs_sum_to_zero([0, 0]))  # True
print(pairs_sum_to_zero([-1, 1]))  # True
print(pairs_sum_to_zero([-1, 1, 2]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 3]))  # True
print(pairs_sum_to_zero([-1, 1, 2, 4]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 4, 5]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 4, 5, 6]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 4, 5, 6, 7]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 4, 5, 6, 7, 8]))  # False
print(pairs_sum_to_zero([-1, 1, 2, 4, 5, 6, 7, 8, 0]))  # True
print(pairs