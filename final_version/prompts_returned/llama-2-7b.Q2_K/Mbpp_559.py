"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def solve(l):
    """
    :type l: List 'a'
    :rtype: int
    Return the sum of the largest sublist.
    """ # Your Code Here
    res = [0] * len(l)
    for i in range(len(l)):
        min_value = float("-inf")
        max_value = 0
        for j, val in enumerate(l):
            if i == j: continue
            if min(res[i], res[j]) < val and val > max_value:
                max_value = max(max_value, val)
                res[i] = val
    return max_value

if __name__ == '__main__':
    l = [-2, -3, 4, -1, -2, 1, 5, -3]
    res = 7
    print(solve(l))