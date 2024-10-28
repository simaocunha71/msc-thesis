```go
func AntiShuffle(s string) string {
    words := strings.Split(s, " ")
    for i := range words {
        r := []rune(words[i])
        sort.Slice(r, func(i, j int) bool {
            return r[i] < r[j]
        })
        words[i] = string(r)
    }
    return strings.Join(words, " ")
}
```
