```go
func IsPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}

func MakePalindrome(s string) string {
    if IsPalindrome(s) {
        return s
    }
    for i := 1; i <= len(s); i++ {
        if IsPalindrome(s[i:]) {
            return s + Reverse(s[:i])
        }
    }
    return ""
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```