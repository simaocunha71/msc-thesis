```go
func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i, word := range words {
        sortedWord := ""
        chars := strings.Split(word, "")
        sort.Strings(chars)
        sortedWord = strings.Join(chars, "")
        words[i] = sortedWord
    }
    return strings.Join(words, " ")
}
```
