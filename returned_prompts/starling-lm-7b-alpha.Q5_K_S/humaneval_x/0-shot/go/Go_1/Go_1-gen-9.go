
The solution to this problem involves a stack data structure.

At each index of the string, we can do one of two things:

1. If the character at the index is an opening parenthesis ( '(' ) , we push it onto the stack.
2. If the character at the index is a closing parenthesis ( ')' ) , we do the following:
   - If the stack is empty, this closing parenthesis is not properly balanced, and we return an error.
   - If the stack is not empty, we pop the most recent opening parenthesis off of the stack.
   - If we have popped an opening parenthesis but there are still parentheses left on the stack, this closing parenthesis is not properly balanced, and we return an error.

The only way for the stack to be empty at the end of the iteration is if the string is properly balanced, and the only way for us to pop all of the opening parentheses off of the stack is if the opening and closing parentheses match up properly.

Here is a working solution in Go:

```go
package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	result := []string{}
	stack := []rune{}

	for _, char := range paren_string {
		if char == '(' {
			stack = append(stack, char)
		} else if char == ')' {
			if len(stack) == 0 {
				return nil
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}

	if len(stack) != 0 {
		return nil
	}

	return result
}
```

And here is the same solution in Python:

```python
def SeparateParenGroups(paren_string):
	result = []
	stack = []

	for char in paren_string:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if len(stack) == 0:
			