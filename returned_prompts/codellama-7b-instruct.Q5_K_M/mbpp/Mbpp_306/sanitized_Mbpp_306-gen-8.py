def max_sum_increasing_subseq(A, i, k, x):
    """
    :param A: input array
    :param i: index of the element
    :param k: index of the element after i
    :param x: element to be added
    :return:
    """
    assert A[i] < A[k]
    A[i] += x
    return max(A[i:k+1])