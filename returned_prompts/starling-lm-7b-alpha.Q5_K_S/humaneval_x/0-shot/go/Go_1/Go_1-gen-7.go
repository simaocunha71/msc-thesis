
To solve this problem, we will use a stack data structure. We will iterate over each character in the input string, and if the character is an open parenthesis '(', we will push the current substring from the last open parenthesis onto the stack. If the character is a close parenthesis ')', we will pop the last string from the stack and append it to the result. If the character is a whitespace character, we will ignore it.

Here is the implementation of the solution:

```go
package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	stack := []string{}
	result := []string{}
	lastOpenIndex := 0
	for i, char := range paren_string {
		if char == '(' {
			lastOpenIndex = i
			currentSubstring := ""
			for ; i < len(paren_string) && paren_string[i] != ')'; i++ {
				currentSubstring += string(paren_string[i])
			}
			stack = append(stack, currentSubstring)
		} else if char == ')' {
			result = append(result, stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}
	}
	return result
}

func main() {
	fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))")) // ["()", "(())", "(()())"]
}
```

In this code, we first initialize an empty stack and an empty result slice. We also initialize a variable `lastOpenIndex` to keep track of the index of the last open parenthesis we encountered. We iterate over each character in the input string using the `range` keyword. If the character is an open parenthesis '(', we update the `lastOpenIndex` to the current index, and initialize a `currentSubstring` variable to store the substring from the last open parenthesis to the current close parenthesis. We then enter a loop that continues until we reach the end of the string or encounter a close parenthesis. In each iteration of the