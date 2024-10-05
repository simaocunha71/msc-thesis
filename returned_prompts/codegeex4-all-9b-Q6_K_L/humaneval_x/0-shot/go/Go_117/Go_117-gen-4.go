```go
func SelectWords(s string, n int) []string {
    result := make([]string, 0)
    words := strings.Fields(s)
    for _, word := range words {
        count := 0
        for _, char := range word {
            if char != 'a' && char != 'e' && char != 'i' && char != 'o' && char != 'u' && char != 'A' && char != 'E' && char != 'I' && char != 'O' && char != 'U' && char != ' ' {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }
    return result
}
```