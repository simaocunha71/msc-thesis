```go
func SelectWords(s string, n int) []string {
    if s == "" {
        return []string{}
    }
    var result []string
    words := strings.Fields(s)
    for _, word := range words {
        consonants := 0
        for _, char := range word {
            if char != 'a' && char != 'e' && char != 'i' && char != 'o' && char != 'u' && char != 'A' && char != 'E' && char != 'I' && char != 'O' && char != 'U' && char != ' ' {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}
```
