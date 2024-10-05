```go
func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i, word := range words {
        sorted := ""
        for _, r := range word {
            sorted += string(r)
        }
        sort.SliceStable([]rune(sorted), func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
        words[i] = sorted
    }
    return strings.Join(words, " ")
}
```