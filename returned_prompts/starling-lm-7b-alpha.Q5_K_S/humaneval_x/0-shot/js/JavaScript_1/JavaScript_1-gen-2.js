Here's a step-by-step breakdown of the solution:

1. Initialize an empty array to store the balanced groups of parentheses.
2. Use a while loop to iterate through the input string.
3. Inside the while loop, use a nested for loop to iterate through each character in the input string.
4. Check if the current character is an open parenthesis '(' and if the stack is not empty. If both conditions are true, push the current index to the stack.
5. If the current character is a closing parenthesis ')' and if the stack is not empty, pop the current index from the stack and store the substring in a variable called 'group'.
6. Check if the 'group' is balanced (i.e., it starts with an open parenthesis '(' and ends with a closing parenthesis ')'). If it is, push the 'group' to the 'result' array.
7. Repeat steps 4-6 until all characters in the input string have been processed.
8. Return the 'result' array containing the balanced groups of parentheses.

Here's the code implementation of the solution:

```python
def separateParenGroups(paren_string):
    result = []
    stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(' and stack:
            stack.append(i)
        elif paren_string[i] == ')':
            if stack:
                start = stack.pop()
                group = paren_string[start:i+1]
                if group.startswith('(') and group.endswith(')'):
                    result.append(group)
    return result
```

The code first initializes an empty list called 'result' to store the balanced groups of parentheses. It also initializes an empty list called 'stack' to keep track of the indices of the opening parentheses.

Then, it uses a while loop to iterate through the input string. Inside the while loop, it uses a nested for loop to iterate through each character in the input string.

The code checks if the current character is an open parenthesis '(' and if the stack is not empty. If both conditions are true, it p