    def pairs_sum_to_zero(l):
        seen = set()
        for x in l:
            if x * -1 in seen:
                return True
            seen.add(x)
        return False
    # test cases
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
    print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
    print(pairs_sum_to_zero([1]))  # False
    print(pairs_sum_to_zero([0, 1]))  # True
    print(pairs_sum_to_zero([0, -1]))  # True
    print(pairs_sum_to_zero([-1, 1]))  # True
    print(pairs_sum_to_zero([1, 1]))  # False
    print(pairs_sum_to_zero([0, 0]))  # True
    print(pairs_sum_to_zero([0, 1, -1]))  # True
    print(pairs_sum_to_zero([-1, 0, 1]))  # True
    print(pairs_sum_to_zero([1, -1, 0, 1]))  # True
    print(pairs_sum_to_zero([1, -1, 2, 3]))  # False
    print(pairs_sum_to_zero([1, -1, 2, -3]))  # True
    print(pairs_sum_to_zero([1, -1, 3, 4]))  # False
    print(pairs_sum_to_zero([1, -1, -3, 4]))  # True
    print(pairs_sum_to_zero([1, -2, 3, 4]))  # False
    print(pairs_sum_to_zero([1, -2, -3, 4]))  # True
    print(pairs_sum_to_zero([1, -2, 3, -4]))  # True
    print(pairs_sum_to_zero([1, -2, -3, -4]))  # False
    print(pairs_sum_to_zero([0, 1, 2, 3, 4,