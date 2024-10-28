Here is the solution using a stack to keep track of the opening and closing parentheses.

```go
import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    var result []int
    var stack []int
    var maxDepth int

    for _, c := range strings.Split(paren_string, " ") {
        depth := 0
        for _, cc := range c {
            if cc == '(' {
                stack = append(stack, depth+1)
                depth++
            } else if cc == ')' {
                stack = stack[:len(stack)-1]
                depth--
            }
            if len(stack) > 0 {
                maxDepth = int(math.Max(float64(maxDepth), float64(depth)))
            }
        }
        result = append(result, maxDepth)
        maxDepth = 0
    }
    return result
}
```

In this function, we iterate over each group of parentheses in the input string, and for each group, we iterate over each character. If we encounter an opening parenthesis, we push the current depth onto the stack and increment the depth. If we encounter a closing parenthesis, we pop the stack and decrement the depth. We keep track of the maximum depth seen so far for each group, and append this to the result array. Finally, we reset the maximum depth for the next group. The function returns the array of maximum depths for each group.