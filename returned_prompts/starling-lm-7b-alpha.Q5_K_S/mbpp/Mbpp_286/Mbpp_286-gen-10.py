"""
def max_sub_array_sum_repeated(array, k, times):
    res = 0
    for i in range(times):
        array = [max(0, j) for j in array]
        if array:
            res = max(res, sum(array))
    return res

# Time complexity: O(n * k)
# Space complexity: O(1)

"""
