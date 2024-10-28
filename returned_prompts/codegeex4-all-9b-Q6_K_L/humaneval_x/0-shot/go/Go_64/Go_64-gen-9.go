```go
func VowelsCount(s string) int {
    vowels := "aeiouAEIOU"
    count := 0
    for _, c := range s {
        if strings.ContainsRune(vowels, c) {
            count++
        }
    }
    if s[len(s)-1] == 'y' || s[len(s)-1] == 'Y' {
        count++
    }
    return count
}
```
