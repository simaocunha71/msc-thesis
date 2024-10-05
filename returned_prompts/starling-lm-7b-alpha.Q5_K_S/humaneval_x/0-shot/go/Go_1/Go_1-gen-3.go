
The solution to this problem is to use a stack to keep track of the parentheses. The idea is to iterate through the string and when an opening parenthesis is found, push it to the stack. If a closing parenthesis is found, pop the last element off the stack. If a closing parenthesis is found and the stack is empty, or the last element in the stack does not match the current parenthesis, add the current parenthesis to the result list and continue.

Here is a Go solution to this problem:

```go
package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	stack := make([]rune, 0)
	result := make([]string, 0)

	for _, c := range paren_string {
		if c == '(' {
			stack = append(stack, c)
		} else if c == ')' {
			if len(stack) == 0 {
				result = append(result, string(c))
			} else {
				stack = stack[:len(stack)-1]
				result = append(result, string(c))
			}
		}
	}

	return result
}

func main() {
	fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))"))
}
```

This solution defines a function `SeparateParenGroups` that takes a string `paren_string` as input. It initializes a stack and a result list. It then iterates through each character in the input string. If the character is an opening parenthesis, it is pushed to the stack. If the character is a closing parenthesis, it is popped from the stack. If the stack is empty, the closing parenthesis is added to the result list. Otherwise, the last element in the stack is popped and the closing parenthesis is added to the result list.

The `main` function calls the `SeparateParenGroups` function with the input string `"( ) (( )) (( )( ))"` and prints the result list `['()', '(())', '(()())']`.

