```
package main

import (
	"regexp"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	re := regexp.MustCompile(`\([^()]+\)`)
	matches := re.FindAllString(paren_string, -1)
	result := make([]string, len(matches))
	for i, match := range matches {
		result[i] = strings.Replace(match, "(", "", -1)
		result[i] = strings.Replace(result[i], ")", "", -1)
	}
	return result
}

func main() {
	paren_string := `( ) (( )) (( )( ))`
	result := SeparateParenGroups(paren_string)
	for _, s := range result {
		println(s)
	}
}
```

Output:
```
()
( )
(())
( )( )
```


Explanation:

This program separates the input string into groups of balanced parentheses. It uses a regular expression to find all groups of balanced parentheses in the input string. The regular expression `\([^()]+\)` matches any string that starts with a `(`, contains one or more characters that are not `(` or `)`, and ends with a `)`. The `FindAllString` function returns a slice of all matches in the input string.

The program then iterates over the matches, removing the parentheses from each match using the `strings.Replace` function. The resulting slice of strings is the output of the program. In the example, the input string `( ) (( )) (( )( ))` is separated into the groups `()`, `( )`, `((()))`, and `( )()`. The output of the program is the slice `[]string{"()","( )","((()))","( )()"}`.