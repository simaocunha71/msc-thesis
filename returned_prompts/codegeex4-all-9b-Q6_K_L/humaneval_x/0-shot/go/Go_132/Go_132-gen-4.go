```go
func IsNested(s string) bool {
    stack := make([]int, 0)
    for _, c := range s {
        if c == '[' {
            stack = append(stack, 1)
        } else if c == ']' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                return false
            }
        }
    }
    return len(stack) == 0
}
```
