```go
func SelectWords(s string, n int) []string {
    if n < 0 || s == "" {
        return []string{}
    }
    words := strings.Fields(s)
    var res []string
    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U' && c != ' ' {
                consonants++
            }
        }
        if consonants == n {
            res = append(res, word)
        }
    }
    return res
}
```
