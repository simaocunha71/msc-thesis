
The problem is asking you to write a function that sorts a list of integers in ascending order based on the sum of their digits. If there are multiple items with the same sum of digits, it should order them based on their original index in the list.

Here is the Python solution:

```
def order_by_points(nums):
    return sorted((sum(int(digit) for digit in str(abs(num))), i, num) for i, num in enumerate(nums))
```

This function uses Python's built-in `sorted` function to sort the list. It uses a tuple for each number in the list, where the first element of the tuple is the sum of the digits of the number, the second element is the index of the number in the original list, and the third element is the number itself. The `sorted` function will first sort based on the first element of the tuple, then by the second element, and finally by the third element. This ensures that numbers with the same sum of digits are ordered based on their original index.

The `enumerate` function is used to get both the index and the value of each number in the list. The `abs` function is used to ensure that the sum of the digits is calculated for the absolute value of the number, since the problem statement does not specify whether the sum should be calculated for the positive or negative value of the number. The `int` function is used to convert each character in the string representation of the number to an integer, and the `sum` function is used to calculate the sum of these integers. The `str` function is used to convert the number to a string, so that it can be iterated over to extract its digits.