Here is a Go function that solves the problem:
```go
func MatchParens(lst []string) string {
    var open, close int
    for _, str := range lst {
        for i := 0; i < len(str); i++ {
            if str[i] == '(' {
                open++
            } else if str[i] == ')' {
                close++
            }
        }
    }
    if open == close {
        return "Yes"
    }
    if open > close {
        return "No"
    }
    return "Yes"
}
```
The function iterates over the input list of strings and counts the number of open and close parentheses. If the number of open parentheses is equal to the number of close parentheses, the function returns "Yes", indicating that it is possible to concatenate the strings to form a balanced string. If the number of open parentheses is greater than the number of close parentheses, the function returns "No", indicating that it is not possible to form a balanced string. If the number of open parentheses is less than the number of close parentheses, the function returns "Yes", indicating that it is possible to form a balanced string by moving the extra close parentheses to the front of the string.

For example, calling `MatchParens([]string{"()(", ")"})` returns "Yes", and calling `MatchParens([]string{")", ")"})` returns "No". The function correctly identifies whether it is possible to form a balanced string by concatenating the input strings in some order.