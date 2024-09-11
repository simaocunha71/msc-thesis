```
def nth_nums(nums, n):
    return [num ** n for num in nums]
```

Explanation:

In this problem, we are asked to compute the n-th power of each number in a list. To solve this problem, we can use a list comprehension to iterate through each number in the input list and calculate its n-th power. The result is a new list containing the n-th power of each number.

Here is an example of how to use the function:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 2
result = nth_nums(nums, n)
print(result)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

In the above code, we define a function called `nth_nums` that takes two arguments: `nums` (the input list) and `n` (the power to raise each number to). The function uses a list comprehension to calculate the n-th power of each number in the `nums` list. The result is a new list that contains the n-th power of each number in the original list.

To use the function, you can pass in your input list and the desired power as arguments. The function will return a new list with the n-th power of each number in the input list.

In the example above, we pass in the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` and the power `2`. The result is a new list `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` which contains the squares of each number in the original list.

The time complexity of this function is O(n) because it iterates through each number in the input list once.

I hope this helps! Let me know if you have any