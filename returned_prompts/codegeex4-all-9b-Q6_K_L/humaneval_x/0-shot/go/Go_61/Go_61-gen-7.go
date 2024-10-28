You can solve this problem by using a stack data structure. Iterate over the string and if the current character is an opening bracket, push it onto the stack. If it's a closing bracket, check if the stack is not empty and the top of the stack is the corresponding opening bracket. If it's not, return false. If the stack is empty after the iteration, return true; otherwise, return false.

Here is the code:

```go
func CorrectBracketing(brackets string) bool {
    stack := make([]rune, 0)
    for _, c := range brackets {
        if c == '(' {
            stack = append(stack, c)
        } else if len(stack) > 0 && stack[len(stack)-1] == '(' {
            stack = stack[:len(stack)-1]
        } else {
            return false
        }
    }
    return len(stack) == 0
}
```

This solution works in O(n) time complexity, where n is the length of the input string.