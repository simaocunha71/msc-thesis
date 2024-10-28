```go
func AntiShuffle(s string) string {
    words := strings.Fields(s)
    for i, word := range words {
        r := []rune(word)
        sort.Slice(r, func(j, k int) bool {
            return r[j] < r[k]
        })
        words[i] = string(r)
    }
    return strings.Join(words, " ")
}
```
