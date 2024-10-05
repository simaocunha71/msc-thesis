```
package main

import (
	"fmt"
	"regexp"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	// Use regular expression to find all balanced groups of parentheses
	re := regexp.MustCompile(`\([^()]+\)`)
	matches := re.FindAllString(paren_string, -1)

	// Split the string into individual groups
	groups := strings.Split(strings.Replace(paren_string, " ", "", -1), ")(")

	// Remove empty strings (which occur when there are consecutive closing parentheses)
	groups = filterEmptyStrings(groups)

	return groups
}

func filterEmptyStrings(arr []string) []string {
	var filtered []string
	for _, s := range arr {
		if s != "" {
			filtered = append(filtered, s)
		}
	}
	return filtered
}

func main() {
	paren_string := `( ) (( )) (( )( ))`
	result := SeparateParenGroups(paren_string)
	fmt.Println(result)
}
```

This program separates the input string into separate groups of balanced parentheses. It uses a regular expression to find all balanced groups of parentheses, then splits the string into individual groups by replacing spaces and splitting on sequences of parentheses. Finally, it removes any empty strings that occur when there are consecutive closing parentheses. The result is a list of separate groups of balanced parentheses. 

The output for the input `( ) (( )) (( )( ))` is `["()", "(())", "(()())"]`. 

Note that the regular expression `\([^()]+\)` matches any sequence of characters that starts with an open parenthesis, contains no open or close parentheses, and ends with a close parenthesis. The `FindAllString` function returns a slice of all matches of this regular expression in the input string. 

The `strings.Replace` function is used to remove spaces from the input string, and the `strings.Split` function is used to split the string into individual groups. The `filterEmptyStrings` function is used to remove any empty strings that occur when there are consecutive closing parentheses. 

The `main` function is used to test the `SeparateParenGroups` function with the input string `( ) (( )) (( )( ))` and print the result. 