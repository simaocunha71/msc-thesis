    var result []int
    groups := strings.Split(paren_string, " ")

B:
    for _, group := range groups {
        maxDepth := 0
        currentDepth := 0
        for _, char := range group {
            switch char {
            case '(':
                currentDepth++
                if currentDepth > maxDepth {
                    maxDepth = currentDepth
                }
            case ')':
                currentDepth--
            }
        }
        result = append(result, maxDepth)
    }

C:
    return result
}

func main() {
    fmt.Println(ParseNestedParens("(()()) ((())) () ((())()())"))
}

*/

import (
	"fmt"
	"strings"
)

// Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
// For each of the group, output the deepest level of nesting of parentheses.
// E.g. (()()) has maximum two levels of nesting while  ((())) has three.
func ParseNestedParens(paren_string string) []int {
	var result []int
	groups := strings.Split(paren_string, " ")

	for _, group := range groups {
		maxDepth := 0
		currentDepth := 0
		for _, char := range group {
			switch char {
			case '(':
				currentDepth++
				if currentDepth > maxDepth {
					maxDepth = currentDepth
				}
			case ')':
				currentDepth--
			}
		}
		result = append(result, maxDepth)
	}
	return result
}

func main() {
	fmt.Println(ParseNestedParens("(()()) ((())) () ((())()())"))
}

/*
Output:
[2, 3, 1, 3]
*/

/*

This Go program accepts a string of groups of parentheses, separated by spaces, and returns the maximum depth of each group of parentheses. 

This is done by iterating through each group, and for each group, iterating through each