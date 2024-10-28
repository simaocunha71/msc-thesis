```go
func Histogram(test string) map[rune]int {
    hist := make(map[rune]int)
    if len(test) == 0 {
        return hist
    }

    words := strings.Fields(test)
    for _, word := range words {
        for _, letter := range word {
            hist[letter]++
        }
    }

    return hist
}
```