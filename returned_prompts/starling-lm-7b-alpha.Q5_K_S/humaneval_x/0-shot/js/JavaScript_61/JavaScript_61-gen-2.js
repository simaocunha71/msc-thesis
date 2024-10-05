Here's a solution in Python:

```python
def correctBracketing(brackets):
    stack = []
    for char in brackets:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
```

This solution uses a stack to keep track of opening brackets. It iterates through each character in the input string `brackets`. If the character is an opening bracket ('('), it is added to the stack. If the character is a closing bracket (')'), it checks if the stack is empty. If the stack is empty, it means there is no corresponding opening bracket for the closing bracket, so it returns `False`. Otherwise, it removes the last opening bracket from the stack. After iterating through all the characters, if the stack is empty, it means all opening brackets have been matched with closing brackets, so it returns `True`. Otherwise, it returns `False`.

This solution has a time complexity of O(n), where n is the length of the input string `brackets`, as it iterates through each character once.

Here's an example usage of the function:

```python
print(correctBracketing("("))  # Output: False
print(correctBracketing("()"))  # Output: True
print(correctBracketing("(()())"))  # Output: True
print(correctBracketing(")(()"))  # Output: False
```

The `correctBracketing` function correctly identifies whether the input string `brackets` has correctly matched opening and closing brackets or not.







/* brackets is a string of "(" and ")".
  return true if every opening bracket has a corresponding closing bracket.

  >>> correctBracketing("(")
  false
  >>> correctBracketing("()")
  true
  >>> correctBracketing("(()())")
  true
  >>> correctBracketing(")(()")
  false
  */

*/













