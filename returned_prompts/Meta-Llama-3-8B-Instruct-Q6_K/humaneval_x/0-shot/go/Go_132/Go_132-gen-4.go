```go
func IsNested(s string) bool {
    stack := make([]rune, 0)
    for _, c := range s {
        if c == '[' {
            stack = append(stack, c)
        } else if c == ']' {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) > 0
}
```

This function uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If it is, it means there's no matching opening bracket and the function returns false. If the stack is not empty, it pops the opening bracket from the stack. Finally, the function checks if there are any opening brackets left in the stack. If there are, it means there's at least one nested bracket and the function returns true. If there aren't, it means there are no nested brackets and the function returns false.