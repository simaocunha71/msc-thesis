```go
func MakePalindrome(str string) string {
    if IsPalindrome(str) {
        return str
    }
    runes := []rune(str)
    for i := len(runes); i > 0; i-- {
        if IsPalindrome(string(runes[i:])) {
            return str + string(reverse(runes[:i]))
        }
    }
    return str
}

func reverse(runes []rune) []rune {
    for i, j := 0, len(runes) - 1; i < j; i, j = i + 1, j - 1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return runes
}
```
