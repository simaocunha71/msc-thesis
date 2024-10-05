```go
func VowelsCount(s string) int {
    count := 0
    vowels := "aeiouy"
    for _, char := range strings.ToLower(s) {
        if strings.ContainsRune(vowels, char) {
            count++
        }
    }
    return count
}
```
