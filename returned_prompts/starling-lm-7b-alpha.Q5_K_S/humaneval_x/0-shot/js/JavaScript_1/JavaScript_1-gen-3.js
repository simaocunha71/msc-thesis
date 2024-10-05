To solve this problem, we can use a stack to keep track of the parentheses.
We iterate through the string, and if we encounter an opening parenthesis, we push it onto the stack.
If we encounter a closing parenthesis, we pop the top element from the stack and check if it is a match.
If it is, we add the current string to the result, otherwise, we add the popped parenthesis to the result.
If the stack is empty, we add the entire string to the result.

Here's a step-by-step breakdown of the solution:

1. Initialize an empty stack and an empty result array.
2. Iterate through the input string.
3. If the current character is an opening parenthesis '(', push it onto the stack.
4. If the current character is a closing parenthesis ')', pop the top element from the stack and check if it is a match. If it is, add the current string to the result. Otherwise, add the popped parenthesis to the result. If the stack is empty, add the entire string to the result.
5. Repeat steps 3-4 until all characters in the input string have been processed.
6. Return the result array.

In the example provided, the function separateParenGroups('( ) (( )) (( )( ))') would return ['()', '(())', '(()())'].

Here's a Python implementation of the solution:

```python
def separateParenGroups(paren_string):
    stack = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result.append(stack.pop())
            else:
                result.append(char)

    if stack:
        result.append(''.join(stack))

    return result
```

This implementation uses a while loop to iterate through the input string and a for loop to iterate through the result array. The time complexity of this solution is O(n), where n is the length of the input string.

The space complexity of this solution is also O(