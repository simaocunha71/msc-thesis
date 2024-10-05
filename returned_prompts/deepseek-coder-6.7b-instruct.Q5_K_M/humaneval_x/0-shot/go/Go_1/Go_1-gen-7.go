
1. Initialize an empty list to hold the separate groups.
2. Remove all spaces from the input string.
3. Initialize a variable to keep track of the current group.
4. Initialize a counter variable to keep track of the number of open parentheses.
5. Loop through each character in the string.
    a. If the character is an open parenthesis, increment the counter.
    b. If the character is a close parenthesis, decrement the counter.
    c. If the counter is 0, the group is complete. Append the current group to the list and start a new group.
6. Return the list of separate groups.
*/

package main

import (
	"fmt"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	var result []string
	paren_string = strings.ReplaceAll(paren_string, " ", "")
	currentGroup := ""
	openCount := 0
	for _, char := range paren_string {
		if string(char) == "(" {
			openCount++
			currentGroup += string(char)
		} else if string(char) == ")" {
			openCount--
			currentGroup += string(char)
			if openCount == 0 {
				result = append(result, currentGroup)
				currentGroup = ""
			}
		}
	}
	return result
}

func main() {
	fmt.Println(SeparateParenGroups("(  )  (( ))  (( )( ))"))
}

// Output:
// [() (()) (()())]

/*
This solution works by iterating over each character in the string. When it encounters an open parenthesis, it increments a counter and adds it to the current group string. When it encounters a close parenthesis, it decrements the counter and adds it to the current group string. When the counter reaches 0, it means the current group is complete, so it adds the group to the result list and starts a new group.
*/
