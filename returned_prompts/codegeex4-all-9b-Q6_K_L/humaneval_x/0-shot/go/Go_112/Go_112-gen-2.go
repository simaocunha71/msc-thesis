```go
func ReverseDelete(s,c string) [2]interface{} {
    var res string
    for _, x := range s {
        if !strings.ContainsRune(c, x) {
            res += string(x)
        }
    }
    rev := ""
    for _, x := range res {
        rev = string(x) + rev
    }
    return [2]interface{}{res, res == rev}
}
```