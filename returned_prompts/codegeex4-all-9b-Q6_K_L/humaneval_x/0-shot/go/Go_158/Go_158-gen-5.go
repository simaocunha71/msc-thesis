```go
func FindMax(words []string) string {
    uniqueCount := func(word string) int {
        unique := make(map[rune]bool)
        for _, c := range word {
            unique[c] = true
        }
        return len(unique)
    }

    max := -1
    result := ""
    for _, word := range words {
        count := uniqueCount(word)
        if count > max || (count == max && word < result) {
            max = count
            result = word
        }
    }
    return result
}
```
