You can use a stack to solve this problem. The idea is to push every opening bracket to the stack and when we encounter a closing bracket, we pop an opening bracket from the stack. If the stack is empty after processing the entire string, then it means every opening bracket had a corresponding closing bracket. Here's how you can implement it in Go:

```go
import (
    "strings"
)

func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, c := range brackets {
        if strings.ContainsRune("([{", c) {
            stack = append(stack, c)
        } else if len(stack) == 0 || !strings.ContainsRune(")]}", stack[len(stack)-1]) {
            return false
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This function goes through each character in the input string. If it's an opening bracket, it pushes it to the stack. If it's a closing bracket, it checks if the top of the stack is the corresponding opening bracket. If it is, it pops the top of the stack. If it's not, or if the stack is empty, it returns false. Finally, it checks if the stack is empty after processing the entire string. If it is, it means every opening bracket had a corresponding closing bracket, so it returns true. Otherwise, it returns false.