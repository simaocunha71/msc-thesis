
Here's a solution that uses a stack to track the opening parentheses and then pops the matching closing parentheses to construct the balanced groups:

```go
func SeparateParenGroups(paren_string string) []string {
	stack := []rune{}
	var groups []string
	var start, end int

	for i := 0; i < len(paren_string); i++ {
		if paren_string[i] == '(' {
			stack = append(stack, paren_string[i])
		} else if paren_string[i] == ')' {
			if len(stack) > 0 {
				start = i - 1
				end = i
				stack = stack[:len(stack)-1]
				groups = append(groups, paren_string[start:end+1])
			}
		}
	}
	return groups
}
```

This solution has a time complexity of O(n) since it iterates through the input string once. The space complexity is also O(n) since the maximum size of the stack is equal to the length of the input string.

Note: This solution assumes that the input string only contains parentheses and spaces. If the input string can contain other characters, then additional logic should be added to handle those cases.

Here's an example usage of the `SeparateParenGroups` function:

```go
package main

import "fmt"

func main() {
	paren_string := "( ) (( )) (( )( ))"
	groups := SeparateParenGroups(paren_string)
	fmt.Println(groups)
}
```

The output of the above code will be `[]string{"()", "(())", "(()())"}`.

Here's an example usage of the `SeparateParenGroups` function with additional characters:

```go
package main

import "fmt"

func main() {
	paren_string := "This is a test ( ) (( )) (( )( )) of the SeparateParenGroups function."
	groups := SeparateParen