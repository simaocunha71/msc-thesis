```go
func CountUpper(s string) int {
    count := 0
    for i := 0; i < len(s); i += 2 {
        if strings.ContainsRune("AEIOU", rune(s[i])) {
            count++
        }
    }
    return count
}
```
