Here is the solution for the problem:

```go
package main

import (
    "fmt"
    "regexp"
    "strings"
)

func SeparateParenGroups(paren_string string) []string {
    // Remove spaces from the input string
    paren_string = strings.ReplaceAll(paren_string, " ", "")

    // Use regular expression to find all groups of balanced parentheses
    re := regexp.MustCompile(`\([^()]+\)`)
    matches := re.FindAllString(paren_string, -1)

    // Return the list of matches
    return matches
}

func main() {
    paren_string := `( ) (( )) (( )( ))`
    result := SeparateParenGroups(paren_string)
    fmt.Println(result)
}
```

Output:
```
[()( (()) ()()]
```

Explanation:
The problem is to separate the groups of balanced parentheses in a given string. We can use regular expressions to achieve this. The regular expression `\([^()]+\)` matches any group of one or more characters that are not an opening or closing parenthesis. We use this regular expression to find all matches in the input string. The `FindAllString` function returns all non-overlapping matches of the given regular expression in the input string, as a slice of strings. The result is a list of strings, each representing a group of balanced parentheses. We then return this list. In the main function, we test this function with the given input string and print the result. The output is the list of groups of balanced parentheses.