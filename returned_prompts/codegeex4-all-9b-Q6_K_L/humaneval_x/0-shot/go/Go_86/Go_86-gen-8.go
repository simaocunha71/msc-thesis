```go
func AntiShuffle(s string) string {
    words := strings.Fields(s)
    for i, word := range words {
        chars := []rune(word)
        sort.Slice(chars, func(j, k int) bool {
            return chars[j] < chars[k]
        })
        words[i] = string(chars)
    }
    return strings.Join(words, " ")
}
```
