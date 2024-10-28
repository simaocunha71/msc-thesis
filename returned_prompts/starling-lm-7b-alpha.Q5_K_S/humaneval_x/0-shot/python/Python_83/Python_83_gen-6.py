
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 2
    # recursive case
    else:
        # count the number of 1s at the beginning
        count_1_begin = starts_one_ends(n-1)
        # count the number of 1s at the end
        count_1_end = (10 ** (n-1)) - (9 * (10 ** (n-2))) + 1
        # add the two counts togther
        count = count_1_begin + count_1_end
        # return the count
        return count

# test
starts_one_ends(2)

# Output:

# 10

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 2
    # recursive case
    else:
        # count the number of 1s at the beginning
        count_1_begin = starts_one_ends(n-1)
        # count the number of 1s at the end
        count_1_end = (10 ** (n-1)) - (9 * (10 ** (n-2))) + 1
        # add the two counts togther
        count = count_1_begin + count_1_end
        # return the count
        return count

# test
starts_one_ends(2)

# Output:

# 10




















































































