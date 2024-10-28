The problem is asking to check if it's possible to concatenate two strings of parentheses in some order, resulting in a balanced string. A string is considered balanced if it has the same number of opening and closing parentheses.

The function takes a slice of two strings as an input, each string consisting of only open parentheses '(' or close parentheses ')'. It returns 'Yes' if it's possible to make a balanced string, and 'No' otherwise.

Here's the solution in Go:
```go
func MatchParens(lst []string) string {
    stack := make([]byte, 0)
    for _, s := range lst {
        for i := 0; i < len(s); i++ {
            if s[i] == '(' {
                stack = append(stack, '(')
            } else if len(stack) > 0 {
                stack = stack[:len(stack)-1]
            } else {
                return "No"
            }
        }
    }
    if len(stack) > 0 {
        return "No"
    }
    return "Yes"
}
```
Here's an explanation of the solution:

1. We use a stack to keep track of the opening parentheses. When we encounter a closing parenthesis, we check if the stack is empty. If it's not empty, we pop the opening parenthesis from the stack. If it's empty, we return "No" because there's no matching opening parenthesis.
2. After processing both strings, we check if the stack is empty. If it's not empty, it means there are unmatched opening parentheses, so we return "No". If it's empty, it means all parentheses are balanced, so we return "Yes".

Let's test the function with the examples:
```go
fmt.Println(MatchParens([]string{"()(", ")"})) // Output: Yes
fmt.Println(MatchParens([]string{")", ")"})) // Output: No
```
The function correctly returns 'Yes' for the first example and 'No' for the second example.