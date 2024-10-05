```go
func Histogram(test string) map[rune]int {
    if test == "" {
        return map[rune]int{}
    }
    histogram := make(map[rune]int)
    words := strings.Fields(test)
    for _, word := range words {
        for _, char := range word {
            histogram[char]++
        }
    }
    maxCount := 0
    for _, count := range histogram {
        if count > maxCount {
            maxCount = count
        }
    }
    result := make(map[rune]int)
    for char, count := range histogram {
        if count == maxCount {
            result[char] = count
        }
    }
    return result
}
```