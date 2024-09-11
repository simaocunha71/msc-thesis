def sum_negativenum(nums):
    return sum([x for x in nums if x < 0])


# Test
assert(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32)


# Other solutions
# def sum_negativenum(nums):
#     return sum(x for x in nums if x < 0)

# def sum_negativenum(nums):
#     return sum(x for x in nums if x < 0)

# def sum_negativenum(nums):
#     return sum(filter(lambda x: x < 0, nums))

```

In this problem, we need to calculate the sum of all the negative numbers in the list, so we need to filter out all the negative numbers first and then calculate the sum. In Python, we can use list comprehension to achieve this. The code `[x for x in nums if x < 0]` is used to filter out all the negative numbers from the given list. Then we use the `sum()` function to calculate the sum of these negative numbers.
```

```
In addition, there are several other ways to solve this problem. For example, we can use the `filter()` function to filter out all the negative numbers from the given list, and then use the `sum()` function to calculate the sum of these negative numbers. Another option is to use a lambda function to filter out all the negative numbers from the given list, and then use the `sum()` function to calculate the sum of these negative numbers.
```

```

```