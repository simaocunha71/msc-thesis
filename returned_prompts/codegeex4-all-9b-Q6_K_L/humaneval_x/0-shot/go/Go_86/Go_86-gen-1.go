```go
func AntiShuffle(s string) string {
    words := strings.Fields(s)
    for i, word := range words {
        sorted := make([]rune, 0, len(word))
        for _, c := range word {
            sorted = append(sorted, c)
        }
        sort.Slice(sorted, func(j, k int) bool {
            return sorted[j] < sorted[k]
        })
        words[i] = string(sorted)
    }
    return strings.Join(words, " ")
}
```