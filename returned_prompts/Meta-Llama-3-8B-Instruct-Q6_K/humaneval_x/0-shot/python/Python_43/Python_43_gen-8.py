def pairs_sum_to_zero(l):
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
    # test your function
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
    print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
    print(pairs_sum_to_zero([1]))  # False
    print(pairs_sum_to_zero([]))  # False
    print(pairs_sum_to_zero([0]))  # False
    print(pairs_sum_to_zero([-1, 1]))  # True
    print(pairs_sum_to_zero([-1, -2, 3]))  # True
    print(pairs_sum_to_zero([-1, 2, 3]))  # True
    print(pairs_sum_to_zero([1, 2, 3, 4]))  # False
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5, 6]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5, 6, 7]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5, 6, 7, 8]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))  # True
    print(pairs_sum_to_zero([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # True
    print(pairs