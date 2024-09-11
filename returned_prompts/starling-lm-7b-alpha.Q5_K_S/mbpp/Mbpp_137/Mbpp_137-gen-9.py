Here's a solution using Python's built-in `count` function:
```python
def zero_count(nums):
    return len([i for i in nums if i == 0]) / len(nums)
```
This function iterates over each number in the input array and counts the number of zeroes by checking if `i` equals `0`. The `count` function returns the number of times the `if` statement returns `True` and uses this to calculate the ratio of zeroes to non-zeroes.

Here's a step-by-step breakdown of the function:

1. The function `zero_count` takes an array of integers called `nums`.
2. It initializes an empty list comprehension `[i for i in nums if i == 0]`. This list comprehension iterates over each number `i` in `nums` and checks if `i` equals `0`. If `i` equals `0`, it adds `i` to the list comprehension.
3. The `len` function is used to find the length of the list comprehension. This gives us the count of zeroes in the array.
4. The `len` function is also used to find the length of the input array `nums`. This gives us the total count of all numbers in the array.
5. The ratio of zeroes to non-zeroes is calculated by dividing the count of zeroes by the total count of numbers in the array. This result is returned by the function.

The `math.isclose` function is used to compare the result of the `zero_count` function with the expected result of `0.181818` within a tolerance of `0.001`. This ensures that the function is accurately calculating the ratio of zeroes to non-zeroes in the array.

Overall, this solution provides an efficient and accurate way to calculate the ratio of zeroes to non-zeroes in an array of integers using Python's built-in `count` function and `math.isclose` function.

Here's an example of how to use the `zero_count` function:
```python
nums = [0, 1, 2, -1, -5, 6, 0, -