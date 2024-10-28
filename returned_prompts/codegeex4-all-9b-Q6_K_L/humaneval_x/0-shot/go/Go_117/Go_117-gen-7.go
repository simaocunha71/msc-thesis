```go
func SelectWords(s string, n int) []string {
    if len(s) == 0 {
        return []string{}
    }
    words := strings.Fields(s)
    res := []string{}
    for _, word := range words {
        count := 0
        for _, c := range word {
            if c >= 'a' && c <= 'z' && !strings.ContainsRune("aeiou", c) {
                count++
            }
        }
        if count == n {
            res = append(res, word)
        }
    }
    return res
}
```