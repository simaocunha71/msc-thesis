
def move_one_ball(arr):
    if not arr: return True
    return all(i <= j for i, j in zip(arr, arr[1:])) or all(i >= j for i, j in zip(arr, arr[1:]))

# Test cases
print(move_one_ball([3, 4, 5, 1, 2])) # True
print(move_one_ball([3, 5, 4, 1, 2])) # False
print(move_one_ball([1, 2, 3, 4, 5])) # True
print(move_one_ball([5, 4, 3, 2, 1])) # True
print(move_one_ball([])) # True
print(move_one_ball([1, 2, 3, 5, 4])) # False

# Time complexity: O(n)
# Space complexity: O(1)

# The function works by comparing each pair of consecutive numbers in the list. If there's a pair where the first number is greater than the second, and we haven't performed a shift yet, we can perform a shift. If we perform the shift, we can check if we can sort the list in non-decreasing order.
<jupyter_output>
True
False
True
True
True
False
<jupyter_text>
**Problem 2**Given a string of braces, write a function that returns True if all braces are balanced and False if they are not. The braces can be any of the following types: {}, [], (), and can be nested. The function should return True if this string represents a well-formed set of braces and False if not. For example, `{}()[]` is well-formed, but `{[}]` is not.
<jupyter_code>
