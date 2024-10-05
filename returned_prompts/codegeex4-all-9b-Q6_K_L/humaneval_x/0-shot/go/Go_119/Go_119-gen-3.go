```go
func MatchParens(lst []string) string {
    open := 0
    close := 0

    for _, str := range lst {
        for _, char := range str {
            if char == '(' {
                open++
            } else {
                close++
            }
        }
    }

    if open == close {
        return "Yes"
    }

    return "No"
}
```
