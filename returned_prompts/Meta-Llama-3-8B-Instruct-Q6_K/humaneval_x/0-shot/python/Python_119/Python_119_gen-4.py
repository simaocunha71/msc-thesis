    def match_parens(lst):
        stack = []
        for char in lst[0] + lst[1]:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return 'No'
        if stack:
            return 'No'
        return 'Yes'
    print(match_parens(['()(', ')'])) # Should return 'Yes'
    print(match_parens([')', ')'])) # Should return 'No'














Solutions

The function match_parens takes a list of two strings as input and checks if it's possible to concatenate them in some order to form a good string. A string is considered good if all the parentheses are balanced.

Here's a Python solution for the problem:

```
def match_parens(lst):
    stack = []
    for char in lst[0] + lst[1]:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return 'No'
    if stack:
        return 'No'
    return 'Yes'
```

In this solution, we iterate over the concatenated string. If we encounter an open parenthesis, we push it onto the stack. If we encounter a close parenthesis, we check if the stack is empty. If the stack is empty, it means there's no matching open parenthesis, so we return 'No'. If the stack is not empty, we pop the open parenthesis from the stack. After iterating over the entire string, if the stack is not empty, it means there are unmatched open parentheses, so we return 'No'. If the stack is empty, it means all parentheses are balanced, so we return 'Yes'.

The time complexity of this solution is O(n), where n is the length of the concatenated string. The space complexity is O(n), as in the worst case, the stack can contain n open parentheses.