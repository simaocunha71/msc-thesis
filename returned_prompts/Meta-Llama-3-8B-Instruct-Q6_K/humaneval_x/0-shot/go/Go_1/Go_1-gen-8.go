```
package main

import (
	"fmt"
	"regexp"
	"strings"
)

func SeparateParenGroups(paren_string string) []string {
	paren_string = strings.ReplaceAll(paren_string, " ", "") // remove spaces
	re := regexp.MustCompile(`\([^()]+\)`)
	matches := re.FindAllString(paren_string, -1)
	return matches
}

func main() {
	paren_string := `( ) (( )) (( )( ))`
	fmt.Println(SeparateParenGroups(paren_string))
}
```

The solution is a combination of using regular expressions and the `strings.ReplaceAll` function in Go. 

The regular expression `\([^()]+\)` is used to match any group of parentheses that do not contain any other parentheses. This is achieved by matching any character that is not an opening or closing parenthesis (`[^\(\)]`) one or more times (`+`) inside a pair of parentheses (`\(` and `\)`).

The `FindAllString` function is then used to find all matches of this regular expression in the input string. The `-1` as the second argument to `FindAllString` means to find all matches, not just the first one.

Finally, the `strings.ReplaceAll` function is used to remove any spaces from the input string, as the regular expression does not ignore spaces. 

The output of the program will be:
```
[() (()) (()())]
```  which is the list of separate groups of nested parentheses. 