```go
func CheckIfLastCharIsALetter(txt string) bool {
    if txt == "" {
        return false
    }
    lastChar := txt[len(txt)-1]
    if !strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lastChar) {
        return false
    }
    if len(txt) > 1 && strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", txt[len(txt)-2]) {
        return false
    }
    return true
}
```
