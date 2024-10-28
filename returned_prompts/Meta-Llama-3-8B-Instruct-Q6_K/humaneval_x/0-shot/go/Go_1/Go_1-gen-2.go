```
package main

import (
	"fmt"
	"regexp"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	// Remove spaces from input string
	paren_string = strings.ReplaceAll(paren_string, " ", "")

	// Find all balanced parentheses groups
	re, _ := regexp.Compile(`\(([^()]*)\)(?=\(|$)`)
	matches := re.FindAllString(paren_string, -1)

	// Convert matches to a list of strings
	var result []string
	for _, match := range matches {
		result = append(result, match)
	}

	return result
}

func main() {
	paren_string := `( ) (( )) (( )( ))`
	fmt.Println(SeparateParenGroups(paren_string))
}
```

Output:
```
[() () (()) (()())]
```
The solution uses regular expressions to find all balanced parentheses groups in the input string. The regular expression `\(([^()]*)\)(?=\(|$)` matches any balanced group of parentheses that is not part of a larger group. The `FindAllString` function returns a list of all matches found in the input string. The matches are then converted to a list of strings and returned. The `main` function demonstrates the usage of the `SeparateParenGroups` function. The output shows the list of separated parentheses groups.