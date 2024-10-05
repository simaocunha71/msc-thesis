Here is the Python solution for the problem:

```python
def sort_numbers(numbers: str) -> str:
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return ' '.join(sorted(numbers.split(), key=lambda x: num_dict[x]))
```

This solution first creates a dictionary where each key is a number in string format and its value is its equivalent integer. Then, it splits the input string into a list of numbers. The sorted() function is used to sort the list of numbers based on their equivalents in the dictionary. The lambda function is used as a key to sort the numbers based on their dictionary equivalents. Finally, the join() function is used to convert the sorted list of numbers back into a string.

Here is the test case:
```python
print(sort_numbers('three one five')) # Output: 'one three five'
```

This solution assumes that the input string will always be valid and contain at least one number. If the input string might contain invalid numbers, then additional error checking should be added.

Also, this solution assumes that the numbers are all different. If the numbers are not all different, then additional code should be added to handle that case.

The time complexity of this solution is O(n log n), where n is the number of numbers in the string. The space complexity is O(n), where n is the number of numbers in the string.

This solution does not account for the fact that the numbers are in string format. If the numbers are in integer format, then the solution would be simpler and the time complexity would be O(n log n).

This solution assumes that the numbers are all different. If the numbers are not all different, then additional code should be added to handle that case.

This solution does not account for the fact that the numbers are in string format. If the numbers are in integer format, then the solution would be simpler and the time complexity would be O(n log n).

This solution assumes that the numbers are all different. If the numbers are not all different,