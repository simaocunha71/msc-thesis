```go
func AntiShuffle(s string) string {
    words := strings.Fields(s)
    sortedWords := make([]string, len(words))
    for i, word := range words {
        sortedWord := ""
        for _, c := range word {
            sortedWord += string(c)
        }
        sortedWords[i] = sortedWord
    }
    sort.Strings(sortedWords)
    return strings.Join(sortedWords, " ")
}
```