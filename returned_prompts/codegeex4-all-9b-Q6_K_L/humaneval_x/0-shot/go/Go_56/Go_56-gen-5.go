You can solve this by using a stack. Push every opening bracket into the stack and pop one whenever you see a closing bracket. If the stack is empty at the end, then you have a correct bracketing. Here is a possible implementation in Go:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, b := range brackets {
        if b == '<' {
            stack = append(stack, b)
        } else if len(stack) > 0 && stack[len(stack)-1] == '<' {
            stack = stack[:len(stack)-1]
        } else {
            return false
        }
    }
    return len(stack) == 0
}
```

This solution has a time complexity of O(n), where n is the length of the input string.