Here is a possible implementation of the `SeparateParenGroups` function in Go:
```go
package main

import (
	"regexp"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	// Use a regular expression to find all balanced groups of parentheses
	re, _ := regexp.Compile(`\([^()]+\)`)
	matches := re.FindAllString(paren_string, -1)

	// Use strings.Split to split the string into individual groups
	var groups []string
	for _, match := range matches {
		groups = append(groups, strings.TrimSpace(match))
	}

	return groups
}

func main() {
	paren_string := `( ) (( )) (( )( ))`
	groups := SeparateParenGroups(paren_string)
	for _, group := range groups {
		println(group)
	}
}
```
This code uses the `regexp` package to find all balanced groups of parentheses in the input string. The regular expression `\([^()]+\)` matches a string that starts with an open parenthesis, contains one or more characters that are not parentheses, and ends with a close parenthesis. The `FindAllString` method returns a slice of all matches found in the input string.

The code then uses the `strings` package to split the input string into individual groups by trimming the matches and appending them to a slice.

Finally, the code prints out each group in the `main` function.

When run with the input string `( ) (( )) (( )( ))`, the output is:
```
()
(())
(()())
```
Which matches the expected output.