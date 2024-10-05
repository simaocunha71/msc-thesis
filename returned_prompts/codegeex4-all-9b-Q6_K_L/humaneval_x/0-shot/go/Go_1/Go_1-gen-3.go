You can use a stack to solve this problem. Start by iterating over the characters in the string. When you encounter an open parenthesis, push it onto the stack. When you encounter a close parenthesis, pop an element from the stack and add the current substring to the list of results. If the stack is empty when you pop an element, that means the parentheses are not balanced and you should return an empty list. Here's a possible implementation of the function:

```go
func SeparateParenGroups(paren_string string) []string {
    var stack []rune
    var result []string
    var current []rune

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            current = append(current, c)
        } else if c == ')' {
            if len(stack) == 0 {
                return []string{}
            }
            stack = stack[:len(stack)-1]
            current = append(current, c)
            if len(stack) == 0 {
                result = append(result, string(current))
                current = []rune{}
            }
        }
    }

    if len(stack) > 0 {
        return []string{}
    }

    return result
}
```

You can test the function with the provided example:

```go
func main() {
    input := "( ) (( )) (( )( ))"
    output := SeparateParenGroups(input)
    fmt.Println(output) // Output: ['()', '(())', '(()())']
}
```