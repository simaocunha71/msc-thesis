Here is a Go solution to your problem. This solution uses a stack to keep track of the nesting level of parentheses.

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
    var stack []int
    var maxDepth int

    for _, c := range strings.Split(paren_string, " ") {
        depth := 0
        for _, r := range c {
            if r == '(' {
                stack = append(stack, depth+1)
                depth += 1
            } else if r == ')' {
                depth -= 1
                stack = stack[:len(stack)-1]
            }
        }
        maxDepth = maxDepth + depth
        result = append(result, maxDepth)
        maxDepth = 0
        stack = nil
    }
    return result
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

This function works by iterating over each group of parentheses in the input string. For each group, it iterates over each character in the group. If it encounters an opening parenthesis, it pushes the current depth onto the stack and increments the depth. If it encounters a closing parenthesis, it decrements the depth and pops the top of the stack. After iterating over all characters in a group, it calculates the maximum depth of the group by summing the remaining depth in the stack, and appends this to the result. It then resets the stack and maximum depth for the next group. The function returns the result as a slice of integers. The max function is used to calculate the maximum depth of a group. 