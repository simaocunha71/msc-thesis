```go
func CorrectBracketing(brackets string) bool {
    var stack []byte
    for _, b := range brackets {
        if b == '(' {
            stack = append(stack, b)
        } else if len(stack) == 0 || stack[len(stack)-1] != '(' {
            return false
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This function uses a stack to keep track of opening brackets. It iterates through each character in the string. If it encounters an opening bracket, it pushes it onto the stack. If it encounters a closing bracket, it checks if the stack is empty or if the top of the stack is not an opening bracket. If either of these conditions is true, it returns false. If it encounters a closing bracket and the top of the stack is an opening bracket, it pops the opening bracket off the stack. After iterating through the entire string, it checks if the stack is empty. If it is, it returns true, meaning the string has correct bracketing. If the stack is not empty, it returns false, meaning the string has incorrect bracketing.