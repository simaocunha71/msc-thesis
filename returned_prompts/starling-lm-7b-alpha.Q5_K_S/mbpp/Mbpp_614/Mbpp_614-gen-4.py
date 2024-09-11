def cummulative_sum(tuples_list):
    """
    This function will find the cumulative sum of all the values that are present in the given tuple list.
    """
    cumulative_sum = 0
    for t in tuples_list:
        cumulative_sum += sum(t)
    return cumulative_sum

# Test Case
assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30


# Time complexity: O(n)
# Space complexity: O(1)


def cummulative_sum_v2(tuples_list):
    return sum(sum(t) for t in tuples_list)

# Test Case
assert cummulative_sum_v2([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Time complexity: O(n)
# Space complexity: O(1)


def cummulative_sum_v3(tuples_list):
    return sum(sum(t) for t in tuples_list)

# Test Case
assert cummulative_sum_v3([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Time complexity: O(n)
# Space complexity: O(1)


def cummulative_sum_v4(tuples_list):
    return sum(sum(t) for t in tuples_list)

# Test Case
assert cummulative_sum_v4([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Time complexity: O(n)
# Space complexity: O(1)


def cummulative_sum_v5(tuples_list):
    return sum(sum(t) for t in tuples_list)

# Test Case
assert cummulative_sum_v5([(1, 3), (5, 6, 7), (2, 6)]) == 30

# Time complexity: O(n)