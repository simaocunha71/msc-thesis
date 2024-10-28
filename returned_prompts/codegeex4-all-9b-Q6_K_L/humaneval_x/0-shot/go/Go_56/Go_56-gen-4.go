You can use a stack to solve this problem. Iterate through the string, and if you encounter an opening bracket, push it onto the stack. If you encounter a closing bracket, check if the stack is empty or if the top of the stack is not the corresponding opening bracket. If either of these conditions is true, return false. Finally, if the stack is not empty after iterating through the string, return false, otherwise return true.

Here is the solution in Go:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
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

This solution has a time complexity of O(n), where n is the length of the input string.