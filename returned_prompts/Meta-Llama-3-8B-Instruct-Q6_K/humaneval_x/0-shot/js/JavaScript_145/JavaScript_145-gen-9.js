Here is the solution in Python:
```
def orderByPoints(nums):
    nums.sort(key=lambda x: (sum(abs(i) for i in str(x)), nums.index(x)))
    return nums
```
Explanation:
We use the built-in `sort` function and provide a custom sorting key using a lambda function. The key is a tuple where the first element is the sum of the absolute values of the digits of each number, and the second element is the index of the number in the original list. This ensures that numbers with the same sum of digits are sorted based on their original index. We use `str(x)` to convert the number to a string, and `abs(i)` to get the absolute value of each digit. Finally, we return the sorted list.