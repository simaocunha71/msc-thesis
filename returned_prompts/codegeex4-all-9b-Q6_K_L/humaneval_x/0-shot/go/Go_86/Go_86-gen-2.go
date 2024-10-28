```go
func AntiShuffle(s string) string {
    words := strings.Fields(s)
    for i, word := range words {
        sortedWord := ""
        for _, c := range word {
            sortedWord += string(c)
        }
        sortedWordBytes := []byte(sortedWord)
        sort.Slice(sortedWordBytes, func(i, j int) bool {
            return sortedWordBytes[i] < sortedWordBytes[j]
        })
        sortedWord = string(sortedWordBytes)
        words[i] = sortedWord
    }
    return strings.Join(words, " ")
}
```
