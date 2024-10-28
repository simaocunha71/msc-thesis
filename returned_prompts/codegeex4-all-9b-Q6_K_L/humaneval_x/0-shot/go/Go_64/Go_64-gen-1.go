```go
func VowelsCount(s string) int {
    vowels := "aeiou"
    count := 0
    for _, c := range strings.ToLower(s) {
        if strings.ContainsRune(vowels, c) {
            count++
        }
    }
    if strings.HasSuffix(strings.ToLower(s), "y") {
        count++
    }
    return count
}
```
