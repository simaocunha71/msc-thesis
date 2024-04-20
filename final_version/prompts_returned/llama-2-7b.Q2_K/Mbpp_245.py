"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
import math

def bitonic_max(seq):
    i = n = 0
    max_val = -1

    while seq[i] < 0:
        if (n % 2) == 1:
            #print "negative %d, so add sum" % seq[i]
            max_sum += seq[i]
            n -= 1
            i -= 1
        else:
            i += 1
    while max(seq[:i]) > max_val:
        if (n % 2) == 0:
            #print "positive %d, so add sum" % seq[i]
            max_sum += seq[i]
            n -= 1
            i -= 1
        else:
            i += 1
    return max(max_val, max_sum)

# test cases
seq = [-16,-7,-2,9,-8,4,-3,5]
max_val = bitonic_max(seq)
print "Bitonic Max:", max_val