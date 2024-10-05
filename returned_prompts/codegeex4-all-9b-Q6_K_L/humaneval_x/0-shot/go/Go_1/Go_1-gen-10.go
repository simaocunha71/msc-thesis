Here is the solution using Go language:

```go
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var stack []int
    var start int
    for i, c := range paren_string {
        if c == '(' {
            stack = append(stack, i)
        } else if c == ')' {
            if len(stack) > 0 {
                start = stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                result = append(result, paren_string[start:i+1])
            }
        }
    }
    return result
}
```

Explanation:
We use a stack to track the start and end of each group of parentheses. When we encounter an open parenthesis, we push the index of it onto the stack. When we encounter a close parenthesis, we pop the stack and add the substring from the start index to the current index (inclusive) to the result list. We repeat this process until we have processed all characters in the input string.

Note: This solution assumes that the input string is a valid string of parentheses and does not perform any error checking.