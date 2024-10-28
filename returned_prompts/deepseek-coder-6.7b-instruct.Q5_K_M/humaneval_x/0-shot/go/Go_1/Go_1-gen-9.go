
// First, we will create an empty list to store the separate parentheses groups.
// Then, we will replace all the spaces in the input string with no space and iterate over the string.
// If we encounter an open parenthesis, we push a new string to the stack and start a new group.
// If we encounter a close parenthesis, we append the character to the current string in the stack and pop the stack.
// Finally, we return the list of separate parentheses groups.

func SeparateParenGroups(paren_string string) []string {
	groups := []string{}
	paren_string = strings.Replace(paren_string, " ", "", -1)
	stack := []string{}
	current_string := ""
	for _, char := range paren_string {
		if string(char) == "(" {
			stack = append(stack, current_string)
			current_string = ""
		} else if string(char) == ")" {
			current_string = string(char) + stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				current_string = stack[len(stack)-1] + current_string
				stack[len(stack)-1] = current_string
			} else {
				groups = append(groups, current_string)
				current_string = ""
			}
		}
	}
	return groups
}


*/

package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	groups := []string{}
	paren_string = strings.Replace(paren_string, " ", "", -1)
	stack := []string{}
	current_string := ""
	for _, char := range paren_string {
		if string(char) == "(" {
			stack = append(stack, current_string)
			current_string = ""
		} else if string(char) == ")" {
			current_string = string(char) + stack[len(stack)-1]
			