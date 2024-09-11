```
def _sum(nums):
    res = 0
    for num in nums:
        res += num
    return res
```

Explanation:
The function _sum takes an array of numbers as an argument. It initializes a variable res to 0. Then it iterates through each number in the array and adds it to res. Finally, it returns the sum of all the numbers in the array. The provided assert statement checks that the function correctly calculates the sum of the array [1, 2, 3].

You can use the function by calling it with an array of numbers as an argument. For example, if you want to find the sum of the array [1, 2, 3], you can call the function like this: `_sum([1, 2, 3])`. The function will return the sum of the array, which in this case is 6.

Note that the function uses the += operator to add each number to res. This operator adds the value of the right operand to the value of the left operand and assigns the result back to the left operand. This allows the function to efficiently calculate the sum of all the numbers in the array without having to explicitly assign the result of each addition to res.

Overall, the function provides a concise and efficient way to find the sum of an array in Python.

Here are a few additional examples of how you can use the function:

```python
print(_sum([4, 5, 6]))  # Output: 15
print(_sum([-1, 0, 1]))  # Output: 0
print(_sum([7, -2, 3]))  # Output: 8
```

In each of these examples, the function correctly calculates the sum of the given array of numbers.

It's important to note that the function assumes that the input array contains only numeric values. If you pass an array that contains non-numeric values, the function will not produce accurate results. To handle such cases, you may need to add additional logic to check and filter the input array before calculating the sum.

Additionally, the function does not handle arrays with zero length. If you pass an empty array to the function, it will return 0. This is because the sum of an empty array is considered