```go
func Histogram(test string) map[rune]int {
    if test == "" {
        return make(map[rune]int)
    }
    words := strings.Fields(test)
    if len(words) == 1 {
        return map[rune]int{rune(words[0][0]): 1}
    }
    wordCount := make(map[rune]int)
    maxCount := 0
    for _, word := range words {
        for _, c := range word {
            wordCount[c]++
            if wordCount[c] > maxCount {
                maxCount = wordCount[c]
            }
        }
    }
    result := make(map[rune]int)
    for c, count := range wordCount {
        if count == maxCount {
            result[c] = count
        }
    }
    return result
}
```
