Here is the solution using a stack:

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
    groups := strings.Split(paren_string, " ")
    result := make([]int, len(groups))
    for i, group := range groups {
        level := 0
        maxLevel := 0
        for _, char := range group {
            if char == '(' {
                level++
                maxLevel = math.Max(maxLevel, level)
            } else if char == ')' {
                level--
            }
        }
        result[i] = maxLevel
    }
    return result
}
```

In this solution, we first split the input string into individual groups of parentheses. Then for each group, we iterate through the characters and keep track of the current level of nesting using a counter. We also keep track of the maximum level of nesting encountered so far. At the end, we return the maximum level of nesting for each group. This solution has a time complexity of O(n), where n is the total number of characters in the input string. The space complexity is O(1) since we are using a constant amount of space to store the result and the temporary variables.