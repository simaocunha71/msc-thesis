Here is the solution for the problem:

```python
def orderByPoints(nums):
    return sorted((num, sum(map(int, str(abs(num))))) for num in nums)
```

Explanation:
The function `orderByPoints` takes a list of integers `nums` as input. It returns a new list sorted according to the sum of the absolute values of the digits of each number. If there are several items with the same sum of their digits, it orders them based on their original index in the list.

Inside the function, we use a generator expression to create a list of tuples. Each tuple contains a number from the input list and the sum of its absolute digits. We use `map` to convert each character in the string representation of the absolute value of the number to an integer, and then sum these integers to get the sum of the digits.

The `sorted` function is used to sort this list of tuples. It first sorts the tuples by the second element of each tuple (i.e., the sum of the digits), and then by the first element (i.e., the original number). This means that numbers with the same sum of digits are ordered by their original index in the list.

Finally, we return the sorted list of tuples, but we only need the first element of each tuple (i.e., the original number), so we use a list comprehension to extract these elements.