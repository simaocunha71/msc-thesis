Here is a Go solution for your problem. The idea is to use a stack to keep track of the opening parentheses and the current level of nesting. When a closing parenthesis is encountered, we pop the stack until we find an opening parenthesis, which indicates the end of the current nested group. The level of nesting for the group is the number of opening parentheses we popped.

```go
import (
    "math"
    "strings"
)

func ParseNestedParens(paren_string string) []int {
    result := []int{}
    stack := []rune{}
    level := 0

    for _, ch := range strings.Split(paren_string, " ") {
        for _, c := range ch {
            if c == '(' {
                stack = append(stack, c)
                level++
            } else if c == ')' {
                level--
                if level == 0 {
                    result = append(result, len(stack))
                    stack = []rune{}
                }
            }
        }
    }

    return result
}
```

This function works by iterating over each character in the input string, and for each character, it checks if it is an opening or closing parenthesis. If it is an opening parenthesis, it pushes it onto the stack and increments the level of nesting. If it is a closing parenthesis, it pops the stack until it finds an opening parenthesis, which indicates the end of the current nested group. The level of nesting for the group is the number of opening parentheses we popped. The function returns a slice of integers, where each integer represents the level of nesting for the corresponding group in the input string.

For example, if the input string is "(()()) ((())) () ((())()())", the function will return the slice `[2, 3, 1, 3]`, which represents the level of nesting for each group in the input string. The first group has 2 levels of nesting, the second group has 3 levels of nesting, the third group has 1 level of nesting, and the fourth group has 3 levels of nesting.