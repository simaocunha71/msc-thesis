```go
func MatchParens(lst []string) string {
    var open, close int
    for _, s := range lst {
        for _, c := range s {
            if c == '(' {
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
