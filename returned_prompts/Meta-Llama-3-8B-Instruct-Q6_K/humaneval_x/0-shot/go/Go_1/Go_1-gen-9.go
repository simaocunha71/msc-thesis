Here is a Go solution to this problem. This function uses a stack to separate the groups of parentheses. It iterates over the input string, pushing opening parentheses onto the stack and popping them off when it encounters a closing parenthesis. When the stack is empty, it means a group has been fully parsed and we add it to the result.

```go
func SeparateParenGroups(paren_string string) []string {
    result := []string{}
    stack := []rune{}
    group := []rune{}

    for _, rune := range paren_string {
        switch rune {
        case '(':
            stack = append(stack, rune)
            group = append(group, rune)
        case ')':
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
                group = append(group, rune)
                if len(stack) == 0 {
                    result = append(result, string(group))
                    group = []rune{}
                }
            }
        }
    }

    return result
}
```

You can test this function with the example you provided:

```go
fmt.Println(SeparateParenGroups("( ) (( )) (( )( ))"))
```

This will output:

```
[ "()", "(())", "(()())" ]
```

This function correctly separates the groups of parentheses in the input string. It ignores any spaces in the input string and only considers the parentheses as separate groups if they are balanced and not nested within each other.