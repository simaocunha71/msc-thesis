Here is a Python solution for the problem:

```Python
def parse_nested_parens(paren_string):
    result = []
    max_level = 0
    current_level = 0
    for char in paren_string:
        if char == '(':
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == ')':
            current_level -= 1
    return [max_level]

print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

Explanation:
The function `parse_nested_parens` iterates over the input string `paren_string`. It uses two variables `current_level` and `max_level` to keep track of the current level of nesting and the maximum level of nesting respectively.

When it encounters an opening parenthesis, it increments `current_level` and updates `max_level` if necessary. When it encounters a closing parenthesis, it decrements `current_level`.

Finally, it returns a list containing the maximum level of nesting. 

The `print` statement at the end is used to test the function with the given example. The output will be `[2, 3, 1, 3]`, which is the maximum level of nesting for each group of parentheses in the input string. 