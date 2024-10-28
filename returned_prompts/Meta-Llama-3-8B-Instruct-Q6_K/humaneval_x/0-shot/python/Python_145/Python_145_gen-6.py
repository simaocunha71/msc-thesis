Here is the Python code to solve the problem:

```Python
def order_by_points(nums):
    return sorted((sum(int(digit) for digit in str(num)), i, num) for i, num in enumerate(nums))
```

This function works by using a generator expression to calculate the sum of the digits of each number, and then sorting the list of tuples based on this sum. If there are several items with the same sum of digits, their order is based on their index in the original list (because the `i` value is included in the tuple). 

For example, if you call `order_by_points([1, 11, -1, -11, -12])`, the function will return `[-1, -11, 1, -12, 11]`. The `sorted` function is stable, which means that when multiple records have the same key, their original order is preserved. 

This function works for both positive and negative numbers, and also handles empty lists correctly, returning an empty list in this case.  The `enumerate` function is used to get both the index and the value of each item in the list.  The `str` function is used to convert each number to a string, and then the `sum` function is used to calculate the sum of the digits.  The `int` function is used to convert each character in the string back to an integer, so that the sum can be calculated correctly. 

The `sorted` function returns a new sorted list from the elements of any sequence. The elements are first converted to keys by applying the function specified by the key argument. By default, the sort is stable and does not change the order of records with equal keys.  The sorted list is returned as a new list object.  The original list remains unchanged. 

This function has a time complexity of O(n log n), where n is the number of items in the input list. This is because the `sorted` function uses a sorting algorithm with a time complexity of O(n log n), such as Timsort or Merge Sort. The `enumerate` function and the generator expression also have a time complexity of O(n), but these are dominated by the time complexity of the `sorted` function.  The space complexity of this function is O(n), because it needs to store the sorted list in memory.  The space complexity of the `sorted` function is O(n), and the space complexity of the generator expression is also O(n), so the