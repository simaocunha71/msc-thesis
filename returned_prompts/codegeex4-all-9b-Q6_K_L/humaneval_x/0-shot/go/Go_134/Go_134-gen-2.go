```go
func CheckIfLastCharIsALetter(txt string) bool {
    if len(txt) == 0 {
        return false
    }
    lastChar := txt[len(txt)-1]
    return strings.LastIndexFunc(txt, func(r rune) bool {
        return !strings.IsLetter(r)
    }) == len(txt)-1 && !strings.IsLetter(lastChar)
}
```
