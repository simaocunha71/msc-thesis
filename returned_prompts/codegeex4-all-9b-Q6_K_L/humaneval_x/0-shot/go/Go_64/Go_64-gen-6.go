```go
func VowelsCount(s string) int {
    vowels := []string{"a", "e", "i", "o", "u", "y"}
    count := 0
    for _, c := range strings.ToLower(s) {
        if strings.Contains(strings.ToLower(string(c)), vowels...) {
            count++
        }
    }
    if len(s) > 0 && strings.ToLower(s[len(s)-1]) == "y" {
        count++
    }
    return count
}
```