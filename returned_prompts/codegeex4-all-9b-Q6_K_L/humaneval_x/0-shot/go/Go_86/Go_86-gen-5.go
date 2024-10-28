```go
func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i, word := range words {
        sortedWord := ""
        for _, c := range word {
            sortedWord += string(c)
        }
        words[i] = sortedWord
    }
    sort.Strings(words)
    return strings.Join(words, " ")
}
```
