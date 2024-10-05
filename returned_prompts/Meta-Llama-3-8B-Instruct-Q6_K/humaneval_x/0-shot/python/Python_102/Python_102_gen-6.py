
This function first generates a list of all even numbers in the range [x, y] using a list comprehension. It then checks if this list is not empty. If it's not empty, it returns the maximum value in the list. If the list is empty (which means there are no even numbers in the range [x, y]), it returns -1.

Here's how you can test this function with the examples you provided:

```
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
```