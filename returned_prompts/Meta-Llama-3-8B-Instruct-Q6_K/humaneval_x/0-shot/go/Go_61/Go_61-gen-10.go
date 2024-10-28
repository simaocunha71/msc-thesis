Here is the solution using a stack:

```go
import (
    "strings"
)

func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range strings.Split(brackets, "") {
        if bracket == "(" {
            stack = append(stack, bracket)
        } else if bracket == ")" {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This function works by iterating over the string of brackets. When it encounters an opening bracket, it pushes it onto the stack. When it encounters a closing bracket, it checks if the stack is empty (which means there's no matching opening bracket) or if the top of the stack is not an opening bracket (which means the brackets are not properly nested). If either of these conditions is true, it returns false. If it finishes iterating over the string and the stack is empty, it returns true, indicating that every opening bracket had a corresponding closing bracket. If the stack is not empty, it returns false, indicating that there was an opening bracket with no corresponding closing bracket.