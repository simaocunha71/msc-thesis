```go
func CheckIfLastCharIsALetter(txt string) bool {
    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    return strings.IndexRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) != -1 && (len(txt) == 1 || txt[len(txt)-2] == ' ')
}
```
