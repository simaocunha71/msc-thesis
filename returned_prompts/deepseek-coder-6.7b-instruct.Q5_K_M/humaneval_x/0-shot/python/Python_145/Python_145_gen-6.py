
def order_by_points(nums):
    return sorted(nums, key=lambda num: (sum(map(int, str(abs(num)))), nums.index(num)))

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))

"""
The function `order_by_points` sorts the list `nums` by the sum of its digits and the original index of the number in `nums`.

For each number in `nums`, it calculates the sum of its digits by converting the absolute value of the number to a string, 
maps `int` over each character of the string to convert them back to integers, and sums the resulting iterable.

The `sorted` function then uses these sums as its sorting key.

If there are multiple numbers with the same sum of digits, `sorted` will use the original index of the numbers in `nums` 
(obtained using `nums.index(num)`) as a fallback sorting key.

If `nums` is empty, the function returns an empty list.
"""

# 2nd Solution:

def order_by_points(nums):
    return sorted(nums, key=lambda num: sum(int(digit) for digit in str(abs(num))))

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))

"""
The function `order_by_points` sorts the list `nums` by the sum of its digits.

For each number in `nums`, it calculates the sum of its digits by converting the absolute value of the number to a string, 
iterates over each character of the string to convert them back to integers, and sums the resulting iterable.

The `sorted` function then uses these sums as its sorting key.

If `nums` is empty, the function returns an empty list.
"""
<jupyter_output>
[-1, 1, 11, -11, -12]