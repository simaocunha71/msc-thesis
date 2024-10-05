Here is a solution in Go:
```go
import (
    "math"
    "strings"
)

// Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
// For each of the group, output the deepest level of nesting of parentheses.
// E.g. (()()) has maximum two levels of nesting while ((())) has three.
// 
// >>> ParseNestedParens('(()()) ((())) () ((())()())')
// [2, 3, 1, 3]
func ParseNestedParens(paren_string string) []int {
    var result []int
    for _, group := range strings.Split(paren_string, " ") {
        level := 0
        maxLevel := 0
        for _, c := range group {
            if string(c) == "(" {
                level++
            } else if string(c) == ")" {
                level--
            }
            if level > maxLevel {
                maxLevel = level
            }
        }
        result = append(result, maxLevel)
    }
    return result
}
```
This solution uses the `strings.Split` function to split the input string into groups separated by spaces. Then, for each group, it uses a loop to iterate over each character. If the character is an opening parenthesis, it increments the level of nesting. If the character is a closing parenthesis, it decrements the level of nesting. It keeps track of the maximum level of nesting seen so far and appends the maximum level to the result slice at the end of processing each group. Finally, it returns the result slice.