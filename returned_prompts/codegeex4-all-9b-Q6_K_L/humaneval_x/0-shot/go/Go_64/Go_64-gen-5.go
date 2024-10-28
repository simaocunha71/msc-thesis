```go
func VowelsCount(s string) int {
    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count := 0
    for _, c := range s {
        if strings.ContainsRune(string(vowels), c) {
            count++
        }
    }
    if len(s) > 0 && strings.HasSuffix(s, "y") {
        count++
    }
    return count
}
```
