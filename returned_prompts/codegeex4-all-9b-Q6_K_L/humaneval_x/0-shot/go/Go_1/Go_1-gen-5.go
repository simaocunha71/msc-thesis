Here is the solution that you can use:

```go
func SeparateParenGroups(paren_string string) []string {
    paren_string = strings.Replace(paren_string, " ", "", -1) // remove spaces
    var result []string
    var stack []string
    for i := 0; i < len(paren_string); i++ {
        if paren_string[i] == '(' {
            stack = append(stack, string(paren_string[i]))
        } else if paren_string[i] == ')' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                // if stack is empty, it means that we have an unbalanced parentheses
                return []string{}
            }
        }
        if len(stack) == 0 && len(paren_string[i:]) > 0 {
            result = append(result, paren_string[i:])
            paren_string = paren_string[i+1:]
            i = -1 // reset the loop to the beginning of the new string
        }
    }
    return result
}
```

This solution uses a stack to keep track of the open parentheses. Whenever we encounter a closing parenthesis, we pop an open parenthesis from the stack. If the stack is empty, it means that we have an unbalanced parentheses. If the stack is empty and there is still a string after the current position, we add the current string to the result and reset the loop to the beginning of the new string. We continue this process until we have processed all the characters in the string.