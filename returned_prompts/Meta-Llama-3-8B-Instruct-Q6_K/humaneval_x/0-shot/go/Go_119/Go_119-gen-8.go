Here is a simple solution in Go. This solution counts the number of open and close parentheses in each string and checks if the counts can be made equal by concatenating the strings in different orders.

```go
func MatchParens(lst []string) string {
    open, close := 0, 0
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
                open++
            } else if c == ')' {
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
    return "No"
}
```

This solution works because if the counts of open and close parentheses are equal, it's possible to concatenate the strings in some order to get a balanced string. If the count of open parentheses is greater than the count of close parentheses, it's not possible to get a balanced string by concatenating the strings in some order. If the count of open parentheses is less than the count of close parentheses, it's also not possible to get a balanced string. Therefore, the function returns "Yes" if the counts are equal, and "No" otherwise.