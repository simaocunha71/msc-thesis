You can use a stack to keep track of the opening brackets. Whenever you encounter a closing bracket, you check if it matches the top of the stack. If it does, you pop the stack. If it doesn't, you return false. At the end, if the stack is empty, you return true. Otherwise, you return false.

Here's the code:

```go
func CorrectBracketing(brackets string) bool {
    stack := make([]rune, 0)
    for _, b := range brackets {
        if b == '<' {
            stack = append(stack, b)
        } else if b == '>' {
            if len(stack) == 0 || stack[len(stack)-1] != '<' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), as we may need to store all opening brackets in the stack.