
You can try to solve this problem by using a stack. Whenever you encounter a '(' character, push it to the stack. When you encounter a ')' character, check if the stack is not empty and if the top of the stack is '(', then pop it from the stack. If the stack is empty or the top of the stack is not '(', then it means the parentheses are not balanced. Finally, if the stack is empty, then the parentheses are balanced, otherwise they are not. Here is the implementation in Go:

```go
func IsBalanced(s string) bool {
    stack := []rune{}
    for _, c := range s {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            if len(stack) == 0 || stack[len(stack)-1] != '(' {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}
```

This solution has a time complexity of O(n), where n is the length of the string. It iterates through the string once and performs a constant amount of work for each character. The space complexity is also O(n), as in the worst case scenario, the stack can contain all the characters in the string.