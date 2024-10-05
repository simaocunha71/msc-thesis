    paren_groups := strings.Fields(paren_string)
    max_levels := make([]int, len(paren_groups))

B:
    for i, group := range paren_groups {
        current_level, max_level := 0, 0
        for _, char := range group {
            if string(char) == "(" {
                current_level++
                if current_level > max_level {
                    max_level = current_level
                }
            } else if string(char) == ")" {
                current_level--
            }
        }
        max_levels[i] = max_level
    }
    return max_levels
}

func main()  {
    fmt.Println(ParseNestedParens("(()()) ((())) () ((())()())"))
}

This program takes a string of parentheses separated by spaces and returns a list of integers representing the maximum depth of nesting for each group. It does this by iterating over each parenthesis group and then each character in the group, counting the depth of nesting. The depth of nesting is reset to zero whenever a closing parenthesis is encountered. The maximum depth of nesting is tracked by comparing it to the current depth at each step.

The time complexity of this program is O(n), where n is the total number of characters in the input string. This is because it performs a single pass over the string. The space complexity is also O(n), as it creates a new list to hold the results.

The program uses the standard libraries strings and fmt for string manipulation and printing.

Note: The function strings.Fields(s string) splits the string s at each run of spaces, returning a slice of substrings. This is used to separate the input string into individual groups of parentheses.
*/

package main

import (
	"fmt"
	"strings"
)

func ParseNestedParens(paren_string string) []int {
	paren_groups := strings.Fields(paren_string)
	max_levels := make([]int, len(paren_groups))

	for i, group := range paren_groups {
	