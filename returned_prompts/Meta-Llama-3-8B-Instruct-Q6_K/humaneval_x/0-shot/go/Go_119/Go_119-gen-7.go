
The problem asks to check if it is possible to concatenate the two strings in some order, that the resulting string will be good. A string S is considered to be good if and only if all parentheses in S are balanced. 

We can use a stack to solve this problem. For each character in the strings, if it's an open parenthesis, we push it to the stack. If it's a close parenthesis, we pop the stack. If the stack is empty or the top of the stack is not an open parenthesis, it means there's no corresponding open parenthesis for the close parenthesis, so we return "No". 

After processing all characters, if the stack is not empty, it means there are some open parentheses without corresponding close parentheses, so we return "No". If the stack is empty, it means all parentheses are balanced, so we return "Yes". 

Here is the code:

```go
func MatchParens(lst []string) string {
    stack := make([]byte, 0)
    for _, str := range lst {
        for _, c := range str {
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
    if len(stack) > 0 {
        return "No"
    }
    return "Yes"
}
```