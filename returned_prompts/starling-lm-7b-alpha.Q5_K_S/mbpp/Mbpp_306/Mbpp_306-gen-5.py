def max_sum_increasing_subseq(seq, i, k, l):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
    >>> max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6)
    11
    """
    # assert that k is greater than i
    assert k > i
    # assert that i is in the list
    assert i in range(len(seq))
    # assert that k is in the list
    assert k in range(len(seq))
    # assert that the seq is a list
    assert isinstance(seq, list) and seq
    # assert that i is a number
    assert isinstance(i, int) and i
    # assert that k is a number
    assert isinstance(k, int) and k
    # assert that l is a number
    assert isinstance(l, int) and l

    max_sum = 0
    for j in range(i, k):
        max_sum += seq[j]
    return max_sum

# Testing
print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6))




"""
def max_sum_increasing_subseq(seq, i, k, l):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
    >>> max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
    True
    """
    # assert that k is greater than i
    assert k > i
    # assert that i is in the list
    assert i in range(len(seq))
    # assert that k is in the list