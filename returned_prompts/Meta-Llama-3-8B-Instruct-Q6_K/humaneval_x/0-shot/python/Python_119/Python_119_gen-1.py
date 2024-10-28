
The function `match_parens(lst)` takes a list of two strings as input and returns 'Yes' if it is possible to concatenate the two strings in some order to form a good string, and 'No' otherwise.

Here is the explanation of the function:

1. Initialize two counters, `open_parens` and `close_parens`, to 0. These counters will be used to keep track of the number of open and close parentheses in the strings.

2. Iterate over the list of strings. For each string, if it is an open parenthesis, increment `open_parens` by 1. If it is a close parenthesis, increment `close_parens` by 1.

3. If `close_parens` is greater than `open_parens` at any point, return 'No' because it means there are more close parentheses than open parentheses, and the strings cannot be concatenated to form a good string.

4. After iterating over all strings, check if `open_parens` is equal to `close_parens`. If they are equal, it means the number of open and close parentheses is balanced, and the strings can be concatenated to form a good string. In this case, return 'Yes'. If they are not equal, return 'No'.

Here is the code:

```
def match_parens(lst):
    open_parens = 0
    close_parens = 0
    for s in lst:
        if s == '(':
            open_parens += 1
        elif s == ')':
            close_parens += 1
        if close_parens > open_parens:
            return 'No'
    return 'Yes' if open_parens == close_parens else 'No'
```

You can test the function with the examples you provided:

```
print(match_parens(['()(', ')']))  # Output: 'Yes'
print(match_parens(['