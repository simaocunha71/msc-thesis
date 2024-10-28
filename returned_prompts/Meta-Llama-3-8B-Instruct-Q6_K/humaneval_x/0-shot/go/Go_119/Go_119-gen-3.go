Here is the solution in Go:
```go
func MatchParens(lst []string) string {
    var stack []rune
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                stack = append(stack, '(')
            } else if c == ')' {
                if len(stack) == 0 || stack[len(stack)-1] != '(' {
                    return "No"
                }
                stack = stack[:len(stack)-1]
            }
        }
    }
    if len(stack) == 0 {
        return "Yes"
    }
    return "No"
}
```
This function uses a stack to keep track of the open parentheses. It iterates over the input list of strings, and for each string, it iterates over the characters. If it encounters an open parenthesis, it pushes it onto the stack. If it encounters a close parenthesis, it checks if the stack is empty or if the top of the stack is not an open parenthesis. If either of these conditions is true, it returns "No". If the stack is empty at the end of the iteration, it returns "Yes", otherwise it returns "No".

The examples you provided:
```go
fmt.Println(MatchParens([]string{"()(", ")"})) // Output: Yes
fmt.Println(MatchParens([]string{")", ")"})) // Output: No
```
Both of these examples are correctly classified as "Yes" and "No" respectively.