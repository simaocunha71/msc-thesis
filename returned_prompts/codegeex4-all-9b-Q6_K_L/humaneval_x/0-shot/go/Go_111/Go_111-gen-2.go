```go
func Histogram(test string) map[rune]int {
    if len(test) == 0 {
        return map[rune]int{}
    }
    m := make(map[rune]int)
    for _, c := range test {
        m[c]++
    }
    maxCount := 0
    for _, count := range m {
        if count > maxCount {
            maxCount = count
        }
    }
    result := make(map[rune]int)
    for c, count := range m {
        if count == maxCount {
            result[c] = count
        }
    }
    return result
}
```