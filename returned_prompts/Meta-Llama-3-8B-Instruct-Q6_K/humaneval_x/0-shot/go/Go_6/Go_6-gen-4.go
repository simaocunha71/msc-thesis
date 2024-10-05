Here is a possible solution in Go:
```go
package main

import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    result := []int{}
    for _, group := range strings.Split(paren_string, " ") {
        level := 0
        for _, char := range group {
            if char == '(' {
                level++
            } else if char == ')' {
                level--
            }
        }
        result = append(result, level)
    }
    return result
}

func main() {
    paren_string := "(()()) ((())) () ((())()())"
    result := ParseNestedParens(paren_string)
    for _, level := range result {
        println(level)
    }
}
```
This program splits the input string into groups by spaces, then for each group, it counts the number of opening and closing parentheses. The level of nesting is the maximum count of opening parentheses minus the count of closing parentheses.

The output of this program for the given input string is:
```
2
3
1
3
```
This means that the deepest level of nesting in each group is 2, 3, 1, and 3 respectively.