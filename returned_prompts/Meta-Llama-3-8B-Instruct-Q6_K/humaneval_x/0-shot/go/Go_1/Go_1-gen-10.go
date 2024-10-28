Here is the solution:

```go
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var group string
    var stack []byte

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            group += string(c)
        } else if c == ')' {
            stack = stack[:len(stack)-1]
            group += string(c)
            if len(stack) == 0 {
                result = append(result, group)
                group = ""
            }
        }
    }
    return result
}
```


Here is the explanation:

We use a stack to keep track of the open parentheses. When we encounter a close parenthesis, we pop the last open parenthesis from the stack. If the stack is empty at this point, it means we have found a complete group of parentheses, and we add it to the result list. We also reset the group string. If the stack is not empty, it means we are still building the current group, and we continue to add the close parenthesis to the group string. Finally, we add the result list to the function return. The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), which is used by the stack and the result list.