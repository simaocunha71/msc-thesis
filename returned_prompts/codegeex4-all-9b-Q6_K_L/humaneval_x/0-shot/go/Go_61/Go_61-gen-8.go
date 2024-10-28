You can use a stack to solve this problem. Iterate over the string and push every opening bracket onto the stack. When you encounter a closing bracket, pop the stack and check if it matches the closing bracket. If it doesn't, or if the stack is empty when you encounter a closing bracket, return false. If you finish iterating over the string and the stack is not empty, return false. Otherwise, return true.

Here's the solution:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, b := range brackets {
        switch b {
        case '(', '[', '{':
            stack = append(stack, b)
        case ')':
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            }
            stack = stack[:len(stack)-1]
        case ']':
            if len(stack) == 0 || stack[len(stack)-1] != '[' {
                return false
            }
            stack = stack[:len(stack)-1]
        case '}':
            if len(stack) == 0 || stack[len(stack)-1] != '{' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), where n is the number of opening brackets in the input string.