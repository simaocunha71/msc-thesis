```go
func FindMax(words []string) string {
    if len(words) == 0 {
        return ""
    }
    var maxWord string
    maxUniqueChars := 0

    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUniqueChars {
            maxUniqueChars = len(uniqueChars)
            maxWord = word
        } else if len(uniqueChars) == maxUniqueChars && word < maxWord {
            maxWord = word
        }
    }
    return maxWord
}
```
