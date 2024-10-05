```
def order_by_points(nums):
    return sorted((sum(int(digit) for digit in str(num)), i, num) for i, num in enumerate(nums))
```
This function uses a generator expression to calculate the sum of the digits for each number in the input list. The `enumerate` function is used to get both the index and the value of each number. The `sorted` function is then used to sort the list of tuples based on the sum of the digits, then by the original index, and finally by the number itself. The result is a list of numbers sorted according to the problem's rules.

Note: In Python, the `sorted` function is stable, meaning that when multiple records have the same key, their original order is preserved. This is why we can sort by the sum of the digits first, and then by the index, and the order of the numbers with the same sum of digits will be preserved.