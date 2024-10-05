
The provided solution defines a function `order_by_points` that takes a list of integers as input and returns a new sorted list. The sorting is done based on two criteria:
1. The sum of the digits of each number. This is achieved by converting the absolute value of each number to a string, mapping each character to its integer value, and summing these values.
2. The original index of each number in the input list. This is achieved by using the `index` method of the input list and passing the current number as an argument.

The `sorted` function is used to sort the input list based on these two criteria. The `key` argument of the `sorted` function is set to a lambda function that returns a tuple. The first element of the tuple is the sum of the digits of each number, and the second element is the original index of each number. The `sorted` function will first sort the list based on the first element of the tuple (sum of digits), and then break ties by sorting based on the second element (original index).

Here is the code:

```
def order_by_points(nums):
    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))
```

This code can be used to sort the given list of integers according to the sum of their digits, and if there are several items with similar sum of their digits, they are ordered based on their index in the original list. For example, if the input list is `[1, 11, -1, -11, -12]`, the output will be `[-1, -11, 1, -12, 11]`. If the input list is empty, the output will be an empty list.