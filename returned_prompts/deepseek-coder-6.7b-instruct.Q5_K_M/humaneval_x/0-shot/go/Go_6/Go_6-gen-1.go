    var depths []int
    groups := strings.Split(paren_string, " ")

B:
    for _, group := range groups {
        count, max := 0, 0

C:
        for _, ch := range group {
            if ch == '(' {
                count++
                max = int(math.Max(float64(max), float64(count)))
            } else if ch == ')' {
                count--
            }
        }
        depths = append(depths, max)
    }
    return depths
}

I've tried to solve this problem in Golang. The function ParseNestedParens takes a string as input and returns a slice of integers.
The function splits the input string into groups separated by spaces, then iterates over these groups. For each group, it counts the number of open and closed parentheses and keeps track of the maximum count at each point, which is the depth of nesting. This maximum count is appended to a slice of integers, which is returned at the end.


A: Here is a version of your function that does what you want. It uses a stack to keep track of the depth of the nested parentheses.

```go
import (
    "strings"
    "strconv"
)

func ParseNestedParens(paren_string string) []int {
    var depths []int
    groups := strings.Split(paren_string, " ")

    for _, group := range groups {
        stack := []int{}
        max := 0

        for _, ch := range group {
            if ch == '(' {
                stack = append(stack, 1)
                if len(stack) > max {
                    max = len(stack)
                }
            } else if ch == ')' {
                if len(stack) > 0 {
                    stack = stack[:len(stack)-1]
                }
            }
        }
        depths = append(depths, max)
    }
    return depths
}
```

This version of the function uses a stack to keep track of the depth of the nested parentheses. The stack is initialized to an empty slice.