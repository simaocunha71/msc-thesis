```go
func MatchParens(lst []string) string {
    var l1, l2 []rune
    for _, s := range lst {
        if len(s) == 0 {
            return "No"
        }
        if len(l1) == 0 {
            l1 = []rune(s)
        } else if len(l2) == 0 {
            l2 = []rune(s)
        } else {
            return "No"
        }
    }
    if len(l1)+len(l2) < 2 {
        return "No"
    }
    if len(l2) > len(l1) {
        l1, l2 = l2, l1
    }
    for _, r := range l1 {
        if r == '(' {
            l2 = append([]rune{')'}, l2...)
        } else {
            if len(l2) == 0 || l2[0] != ')' {
                return "No"
            }
            l2 = l2[1:]
        }
    }
    if len(l2) == 0 {
        return "Yes"
    }
    for _, r := range l2 {
        if r != ')' {
            return "No"
        }
    }
    return "Yes"
}
```
