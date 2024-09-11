from functools import reduce
def max_Product(arr):
    return reduce(lambda x,y: max(x,y) if x*y > 0 else min(x,y), arr)


"""
The above approach will not work if the array contains zero.

Here is the correct approach:

"""

def max_Product(arr):
    if len(arr) < 2:
        return arr
    min_ele, max_ele = min(arr), max(arr)
    if min_ele == max_ele:
        return (min_ele, min_ele)
    max_ele_pair = (max_ele, arr[arr.index(max_ele) - 1])
    if max_ele_pair[0] * max_ele_pair[1] > max_ele:
        return max_ele_pair
    min_ele_pair = (min_ele, arr[arr.index(min_ele) + 1])
    if min_ele_pair[0] * min_ele_pair[1] < min_ele:
        return min_ele_pair
    return max_ele_pair


"""
Alternatively, we can use the following approach:

"""

def max_Product(arr):
    if len(arr) < 2:
        return arr
    min_ele, max_ele = min(arr), max(arr)
    if min_ele == max_ele:
        return (min_ele, min_ele)
    max_ele_pair = (max_ele, arr[arr.index(max_ele) - 1])
    if max_ele_pair[0] * max_ele_pair[1] > max_ele:
        return max_ele_pair
    min_ele_pair = (min_ele, arr[arr.index(min_ele) + 1])
    if min_ele_pair[0] * min_ele_pair[1] < min_ele:
        return min_ele_pair
    return max(max_ele_pair, min_ele_pair)

# Testing
assert max_Product([1,2,3,4,7,0,8