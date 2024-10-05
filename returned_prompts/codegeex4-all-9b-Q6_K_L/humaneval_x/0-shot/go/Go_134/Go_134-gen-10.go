```go
func CheckIfLastCharIsALetter(txt string) bool {
    if txt == "" {
        return false
    }
    lastChar := txt[len(txt)-1]
    return strings.IndexRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) != -1 && !strings.HasSuffix(txt, " ")
}
```
