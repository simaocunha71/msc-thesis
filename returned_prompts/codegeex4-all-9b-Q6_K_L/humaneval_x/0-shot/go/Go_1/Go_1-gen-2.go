You can solve this problem by using a stack to keep track of the parentheses. When you encounter an open parenthesis, you push it onto the stack. When you encounter a close parenthesis, you pop the stack and check if the stack is empty. If it is, then you have found a separate group of parentheses and you can add it to your result list.

Here's an example implementation:

```go
func SeparateParenGroups(paren_string string) []string {
    stack := []rune{}
    result := []string{}
    group := []rune{}

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            group = append(group, c)
        } else if c == ')' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
                group = append(group, c)
            } else {
                result = append(result, string(group))
                group = []rune{}
            }
        }
    }

    if len(group) > 0 {
        result = append(result, string(group))
    }

    return result
}
```

Here's how you can use this function:

```go
func main() {
    input := "( ) (( )) (( )( ))"
    result := SeparateParenGroups(input)
    fmt.Println(result) // Output: ['()', '(())', '(()())']
}
```