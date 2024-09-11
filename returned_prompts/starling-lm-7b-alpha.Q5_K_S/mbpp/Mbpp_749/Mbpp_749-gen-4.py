def sort_numeric_strings(lst):
    return [int(s) for s in sorted(lst)]

# Testing
assert sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]
print("All Tests Passed")



# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
# Here's how it works:
# We use list comprehension to convert each string in the given list into an integer. We use the sorted() function to sort the strings in the list, and then convert them to integers using list comprehension. The sorted() function has a time complexity of O(nlog(n)), and the list comprehension has a time complexity of O(n). Therefore, the overall time complexity is O(nlog(n)).
# The space complexity is O(n) because we create a new list of integers, which requires additional memory.



```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
