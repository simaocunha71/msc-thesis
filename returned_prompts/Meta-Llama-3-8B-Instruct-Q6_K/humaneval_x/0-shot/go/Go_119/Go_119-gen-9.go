```go
func MatchParens(lst []string) string {
    open := 0
    close := 0
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


The idea here is to count the number of open and close parentheses in the given list of strings. If the number of open and close parentheses are equal, it means that we can concatenate the strings in some order to form a valid parentheses string, and we return "Yes". Otherwise, we return "No". This solution is O(n) where n is the total length of the input strings.