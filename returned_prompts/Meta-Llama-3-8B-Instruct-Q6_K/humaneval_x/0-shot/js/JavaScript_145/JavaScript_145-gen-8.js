Here is a Python solution for the problem. The idea is to first calculate the sum of digits for each number, then sort the list based on these sums and the original indices. Python's built-in `sorted` function is used for the sorting:

```python
def orderByPoints(nums):
    if not nums:
        return []

    nums.sort(key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))
    return nums
```

This solution first checks if the input list is empty. If it is, the function returns an empty list. Then it calculates the sum of digits for each number in the list by converting each number to a string, mapping each character in the string to an integer, and summing up these integers. The `abs` function is used to ensure that the sum of digits is calculated for the absolute value of each number, since the problem statement asks for the sum of digits in ascending order.

The `sorted` function is then used to sort the list based on the sums of digits and the original indices of the numbers. The `key` argument of the `sorted` function is a function that takes a list element and returns a value that will be used for sorting purposes. In this case, the `key` function returns a tuple containing the sum of digits for each number and its original index in the list. The `sorted` function will first sort the list based on the sums of digits and then based on the original indices.

Finally, the sorted list is returned. This solution has a time complexity of O(n log n) due to the sorting operation, where n is the number of elements in the input list. The space complexity is O(1) since only a constant amount of space is used. 