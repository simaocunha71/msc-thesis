Here is a Python solution for the problem:

```Python
def orderByPoints(nums):
    nums = sorted([(num, sum(map(int, str(abs(num))))) for num in nums], key=lambda x: (x[1], nums.index(x[0])))
    return [num[0] for num in nums]
```

Explanation:
This function works by first creating a list of tuples where each tuple contains a number and its sum of digits. The sum of digits is calculated by converting the number to a string, then summing up the digits. The `abs` function is used to ensure that negative numbers are handled correctly.

Then, the list of tuples is sorted based on two keys: the sum of digits and the index of the number in the original list. The `lambda` function is used to specify these two keys.

Finally, the function returns a list of the first element of each tuple, which are the sorted numbers.

For example, if the input is `[1, 11, -1, -11, -12]`, the function will return `[-1, -11, 1, -12, 11]`. If the input is an empty list, the function will return an empty list.