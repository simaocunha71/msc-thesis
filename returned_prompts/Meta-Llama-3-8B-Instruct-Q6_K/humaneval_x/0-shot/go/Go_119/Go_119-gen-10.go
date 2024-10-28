Here is the solution:

```go
func MatchParens(lst []string) string {
    stack := make([]byte, 0)
    for _, str := range lst {
        for _, c := range str {
            if c == '(' {
                stack = append(stack, '(')
            } else {
                if len(stack) == 0 || stack[len(stack)-1] != '(' {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) > 0 {
        return "No"
    }
    return "Yes"
}
```

Explanation:

This function uses a stack to keep track of the open parentheses. For each character in the input strings, it checks if it's an open parenthesis or a close parenthesis.

If it's an open parenthesis, it pushes it onto the stack. If it's a close parenthesis, it checks if the stack is empty or the top of the stack is not an open parenthesis. If either of these conditions is true, it returns "No" because the parentheses are not balanced.

After processing all the input strings, it checks if the stack is empty. If it's not empty, it means there are unmatched open parentheses, so it returns "No". If the stack is empty, it returns "Yes" because the parentheses are balanced.

This function has a time complexity of O(n), where n is the total number of characters in the input strings, and a space complexity of O(n) because in the worst case, the stack will store all the open parentheses.