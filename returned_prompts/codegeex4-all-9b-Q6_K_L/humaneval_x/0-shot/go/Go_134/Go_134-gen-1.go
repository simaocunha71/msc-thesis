```go
func CheckIfLastCharIsALetter(txt string) bool {
    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    if 'a' <= lastChar && lastChar <= 'z' || 'A' <= lastChar && lastChar <= 'Z' {
        if len(txt) == 1 || txt[len(txt)-2] == ' ' {
            return true
        }
    }
    return false
}
```
