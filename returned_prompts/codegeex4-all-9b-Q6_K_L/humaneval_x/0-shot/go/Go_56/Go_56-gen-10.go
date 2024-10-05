You can solve this problem by using a stack data structure. Iterate through the string and push every opening bracket into the stack. When you encounter a closing bracket, check if the stack is empty or if the top of the stack is not the corresponding opening bracket. If either of these conditions is true, return false. After iterating through the entire string, if the stack is empty, return true; otherwise, return false.
Here's the solution in Go:

```go
func CorrectBracketing(brackets string) bool {
    stack := []rune{}
    for _, bracket := range brackets {
        if bracket == '<' {
            stack = append(stack, bracket)
        } else if len(stack) == 0 || stack[len(stack)-1] != '<' {
            return false
        } else {
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```
This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.