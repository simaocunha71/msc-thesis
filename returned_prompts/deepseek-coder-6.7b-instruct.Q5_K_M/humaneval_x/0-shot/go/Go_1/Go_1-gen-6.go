
paren_string = strings.ReplaceAll(paren_string, " ", "")

paren_groups := make([]string, 0)

stack := make([]rune, 0)

current_group := make([]rune, 0)

for _, c := range paren_string {

    if c == '(' {

        stack = append(stack, c)

        current_group = append(current_group, c)

    } else if c == ')' {

        stack = stack[:len(stack)-1]

        current_group = append(current_group, c)

        if len(stack) == 0 {

            paren_groups = append(paren_groups, string(current_group))

            current_group = make([]rune, 0)

        }

    }

}

return paren_groups

}

*/

// This code takes a string of parentheses, replaces any spaces, and separates the groups of parentheses into separate strings.
// It does so by utilizing a stack data structure to check if parentheses are balanced.
// The groups of parentheses are then stored in a list.
// If the stack is empty (meaning the parentheses are balanced), the current group of parentheses is added to the list.
// The list of separate parentheses groups is then returned.

package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {

	paren_string = strings.ReplaceAll(paren_string, " ", "")

	paren_groups := make([]string, 0)

	stack := make([]rune, 0)

	current_group := make([]rune, 0)

	for _, c := range paren_string {

		if c == '(' {

			stack = append(stack, c)

			current_group = append(current_group, c)

		} else if c == ')' {

			stack = stack[:len(