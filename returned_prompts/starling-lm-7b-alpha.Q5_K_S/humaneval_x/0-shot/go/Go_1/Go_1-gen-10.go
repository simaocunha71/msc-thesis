
```go
package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	var result []string
	var current_group string
	var depth int
	for _, char := range paren_string {
		if char == '(' {
			depth++
		} else if char == ')' {
			depth--
		} else if char == ' ' {
			continue
		}
		if depth == 0 {
			result = append(result, current_group)
			current_group = ""
		}
		current_group += string(char)
	}
	if current_group != "" {
		result = append(result, current_group)
	}
	return result
}

func main() {
	fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))"))
}
```

In this problem, we are given a string of parentheses (), [], and () that can be nested inside each other. Our goal is to separate these groups into separate strings and return them as a list. In order to do this, we need to determine if each group is balanced and not nested within each other.

To solve this problem, we can start by initializing a result slice to store the separated groups. We also need to keep track of the current_group and the depth of the parentheses. We can use a for loop to iterate through each character in the input string.

Inside the loop, we check if the character is an opening parenthesis ("). If it is, we increment the depth variable by 1. If the character is a closing parenthesis (")), we decrement the depth variable by 1. If the character is a space, we can ignore it and continue to the next character.

After checking the character, we need to determine if the current depth is 0. If it is, it means that we have reached the end of a group and we can append the current_group to the result slice. We reset the current_group to an empty string for the next group.

Once we have iterated through all the characters in the input string