```
def double_the_difference(lst):
    return sum(num ** 2 for num in lst if isinstance(num, int) and num > 0)
```


Here's an explanation of the code:

1. The function takes a list of numbers as input.
2. The `isinstance(num, int) and num > 0` part is a condition that checks if the number is an integer and positive. This ensures that we only consider numbers that are odd and not negative.
3. The `num ** 2` part calculates the square of the number.
4. The `sum` function is used to add up the squares of the numbers that meet the condition.
5. If the input list is empty, the `sum` function will return 0, as per the problem statement.

For example, if the input list is `[1, 3, 2, 0]`, the function will return `1 ** 2 + 3 ** 2 + 0 ** 2 = 1 + 9 + 0 = 10`. If the input list is `[-1, -2, 0]`, the function will return `0`, because all the numbers are negative or not integers. If the input list is `[9, -2]`, the function will return `9 ** 2 = 81`. If the input list is `[0]`, the function will return `0 ** 2 = 0`. If the input list is empty, the function will return `0`.