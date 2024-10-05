Here is a possible implementation of the `SelectWords` function in Go:
```go
func SelectWords(s string, n int) []string {
    words := strings.Split(s, " ")
    result := make([]string, 0)
    for _, word := range words {
        consonants := 0
        for _, r := range strings.ToLower(word) {
            if !strings.Contains("aeiou", string(r