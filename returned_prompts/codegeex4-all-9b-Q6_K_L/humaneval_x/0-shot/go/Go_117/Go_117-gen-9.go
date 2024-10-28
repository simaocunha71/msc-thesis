```go
func SelectWords(s string, n int) []string {
    if s == "" {
        return []string{}
    }

    consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result := []string{}
    words := strings.Fields(s)

    for _, word := range words {
        count := 0
        for _, char := range word {
            if strings.ContainsRune(consonants, char) {
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
