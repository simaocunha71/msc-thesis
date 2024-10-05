```go
func VowelsCount(s string) int {
    vowels := "aeiou"
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count++
        }
    }
    if len(s) > 0 && strings.HasSuffix(s, "y") {
        count++
    }
    return count
}
```