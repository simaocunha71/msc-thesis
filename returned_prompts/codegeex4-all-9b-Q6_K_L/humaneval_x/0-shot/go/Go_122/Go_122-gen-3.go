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
    return sum(int(num) for num in arr[:k] if len(str(num)) <= 2)

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # Output: 24
print(add_elements([1, 2, 3, 4, 5], 3))  # Output: 3
print(add_elements([100, 200, 300, 400, 500], 2))  # Output: 0

C:
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
    return sum(int(num) for num in arr[:k] if len(str(num)) <= 2)

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # Output: 24
print(add_elements([1, 2, 3, 4, 5], 3))  # Output: 3
print(add_elements([100, 200, 300, 400, 500], 2))  # Output: 0

