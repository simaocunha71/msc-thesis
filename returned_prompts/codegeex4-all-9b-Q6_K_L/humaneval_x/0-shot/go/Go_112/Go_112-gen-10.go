```go
func ReverseDelete(s,c string) [2]interface{} {
    s2 := make([]rune, 0, len(s))
    for _, ch := range s {
        if !strings.ContainsRune(c, ch) {
            s2 = append(s2, ch)
        }
    }
    return [2]interface{}{string(s2), isPalindrome(string(s2))}
}

func isPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}
```
