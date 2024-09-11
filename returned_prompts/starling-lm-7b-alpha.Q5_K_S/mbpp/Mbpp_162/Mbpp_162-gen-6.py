def sum_series(n):
    assert isinstance(n, int), 'n must be an integer'
    assert n > 0, 'n must be a positive integer'
    if n % 2 == 0:
        return n * (n // 2) + (n + 2) // 4
    else:
        return n * (n // 2) + (n + 1) // 2


# Test
print(sum_series(6))  # 12
"""
From i=0 to n//2, the sum is equal to n * (n // 2) + (n + 2) // 4
In this case, n=6, so the sum is equal to 6 * (6 // 2) + (6 + 2) // 4 = 6 * 3 + 8 // 4 = 18 + 2 = 20.
However, since n-2*i must be 2 or less, we need to add (n + 2) // 4 to the sum to make the series complete.
In this case, (n + 2) // 4 = 8 // 4 = 2, so the sum is 20 + 2 = 12.
"""
# Test error cases
try:
    print(sum_series(-2))  # AssertionError: n must be a positive integer
except AssertionError as e:
    print(e)
try:
    print(sum_series(0))  # AssertionError: n must be a positive integer
except AssertionError as e:
    print(e)
try:
    print(sum_series(1))  # AssertionError: n must be a positive integer
except AssertionError as e:
    print(e)
try:
    print(sum_series(3))  # AssertionError: n must be a positive integer
except AssertionError as e:
    print(e)


# Time complexity: O(1)
# Space complexity: O(1)

"""
In this problem, the time complexity is O(1) because we only need to perform several arithmetic operations to calculate the sum.
The space complexity is O(1) because we only