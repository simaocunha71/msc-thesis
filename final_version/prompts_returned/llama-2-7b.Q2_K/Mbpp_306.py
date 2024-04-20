"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""

def maximum_sum_from_prefix(prefix, suffix): # (list of integers), (list or integer)
    m = [x for x in suffix]
    max_sofar = prefix[0] if len(prefix) else 0
    for ele in prefix[1:]:
        next_ele = m[0] + ele
        if next_ele > max_sofar:
            max_sofar, max_elem = next_ele, ele
        else:
            max_elem == next_ele
    return max_elem

if __name__ == '__main__':
    prefix = [4] # list of integers
    suffix = [101] # (list or integer)
    print(maximum_sum_from_prefix(prefix, suffix))