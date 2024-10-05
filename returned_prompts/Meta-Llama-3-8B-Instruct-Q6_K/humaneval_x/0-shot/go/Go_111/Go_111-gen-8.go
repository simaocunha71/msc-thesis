```go
func Histogram(test string) map[rune]int {
    if test == "" {
        return map[rune]int{}
    }
    words := strings.Split(test, " ")
    m := make(map[rune]int)
    for _, word := range words {
        for _, char := range word {
            m[char]++
        }
    }
    maxCount := 0
    for k, v := range m {
        if v > maxCount {
            maxCount = v
        }
    }
    result := make(map[rune]int)
    for k, v := range m {
        if v == maxCount {
            result[k] = v
        }
    }
    return result
}
```

This function first splits the input string into words. Then, for each word, it increments the count of each character in a map. After that, it finds the maximum count. Finally, it creates a new map that contains only the characters with the maximum count.

This function returns a map where the keys are the characters and the values are the counts. If there are multiple characters with the same maximum count, they are all included in the result map. If the input string is empty, the function returns an empty map.