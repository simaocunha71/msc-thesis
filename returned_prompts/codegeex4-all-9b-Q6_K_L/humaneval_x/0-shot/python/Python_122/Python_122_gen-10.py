def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total

# Test cases
print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
print(add_elements([1,2,3,4,5,6,7,8,9], 5)) # 15
print(add_elements([1,1,1,1,1,1,1,1,1], 9)) # 9
print(add_elements([9,9,9,9,9,9,9,9,9], 3)) # 18
print(add_elements([999,999,999,999,999,999,999,999,999], 4)) # 1980