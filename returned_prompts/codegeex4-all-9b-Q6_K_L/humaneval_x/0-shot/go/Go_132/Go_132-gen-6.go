Here's one way you can solve this problem:

```go
func IsNested(s string) bool {
    stack := make([]rune, 0)
    for _, c := range s {
        if c == '[' {
            stack = append(stack, c)
        } else if c == ']' {
            if len(stack) > 0 && stack[len(stack)-1] == '[' {
                stack = stack[:len(stack)-1]
            } else {
                return true
            }
        }
    }
    return false
}
```

The idea is to use a stack to keep track of the brackets. If we encounter an opening bracket, we push it onto the stack. If we encounter a closing bracket, we check if the top of the stack is an opening bracket. If it is, we pop it off the stack. If it's not, we know there's a valid subsequence of brackets where at least one bracket is nested, so we return `true`.

If we reach the end of the string and the stack is empty, we know there are no nested brackets, so we return `false`.