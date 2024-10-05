You can use a stack to solve this problem. The idea is to keep track of the starting index of each group of parentheses and push it onto the stack when you encounter an opening parenthesis. When you encounter a closing parenthesis, you pop the stack and add the substring from the current index to the popped index to the result. Here's the solution:

```go
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var stack []int
    for i, c := range paren_string {
        if c == '(' {
            stack = append(stack, i)
        } else if c == ')' {
            if len(stack) > 0 {
                start := stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                result = append(result, paren_string[start:i+1])
            }
        }
    }
    return result
}
```

This solution has a time complexity of O(n), where n is the length of the input string.