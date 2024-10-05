
// We will use a stack data structure to solve this problem.
// We will iterate over each string in the list.
// For each string, we will iterate over each character.
// If the character is an open parenthesis, we will push it into the stack.
// If the character is a close parenthesis, we will pop an element from the stack.
// If the stack is empty, we will return 'No' because it's impossible to close a parenthesis that does not exist.
// If we finish iterating over all characters in all strings without returning 'No', we will return 'Yes' because it's possible to balance the parentheses.

	// Initialize a stack
	stack := []rune{}

	// Iterate over each string in the list
	for _, str := range lst {
		// Iterate over each character in the string
		for _, char := range str {
			// If the character is an open parenthesis, push it into the stack
			if char == '(' {
				stack = append(stack, char)
			} else { // If the character is a close parenthesis
				// If the stack is empty, return 'No'
				if len(stack) == 0 {
					return "No"
				}
				// Pop an element from the stack
				stack = stack[:len(stack)-1]
			}
		}
	}

	// If the stack is empty, return 'Yes'
	if len(stack) == 0 {
		return "Yes"
	}
	// If the stack is not empty, return 'No'
	return "No"
}

*/

package main

import "fmt"

func MatchParens(lst []string) string {
	stack := []rune{}

	for _, str := range lst {
		for _, char := range str {
			if char == '(' {
				stack = append(stack, char)
			} else {
				if len(stack) == 0 {
					return "No"
				}
				stack = stack[:len(stack)-1]
			}
		}
	}

	if len(stack) == 0 {
		return "Yes"
	}
	return "No"
