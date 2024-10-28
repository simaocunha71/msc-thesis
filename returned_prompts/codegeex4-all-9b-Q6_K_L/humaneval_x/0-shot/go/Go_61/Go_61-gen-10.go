You can solve this problem by using a stack. When you encounter an opening bracket, push it onto the stack. When you encounter a closing bracket, check if the stack is empty. If it is, then there is no corresponding opening bracket, so return false. Otherwise, pop the top element from the stack and continue.

Here's the solution in Go:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, b := range brackets {
        if b == '(' {
            stack = append(stack, b)
        } else if len(stack) == 0 {
            return false
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.