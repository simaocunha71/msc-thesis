```python
def parse_nested_parens(paren_string: str) -> List[int]:
    group_list = paren_string.split()
    result = []

    for group in group_list:
        count = 0
        max_count = 0
        for char in group:
            if char == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif char == ')':
                count -= 1
        result.append(max_count)

    return result
```

This function works by splitting the input string into groups of parentheses. For each group, it counts the number of open parentheses '(' and compares it with the maximum count found so far. If the count is greater than the max_count, it updates max_count. The max_count at the end of each group is the maximum depth of nesting for that group. These max_counts are appended to the result list, which is returned at the end.

The time complexity of this function is O(n), where n is the total number of characters in all groups. This is because the function iterates through each character in each group once. The space complexity is also O(n), because a new list of maximum depths is created for each group.

You can test this function using the following code:

```python
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This should output:

```
[2, 3, 1, 3]
```

which is the expected result.
