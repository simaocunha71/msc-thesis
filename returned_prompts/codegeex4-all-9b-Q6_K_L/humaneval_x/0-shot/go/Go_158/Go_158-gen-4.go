```go
func FindMax(words []string) string {
    maxUniques := 0
    maxWord := ""
    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUniques || (len(uniqueChars) == maxUniques && word < maxWord) {
            maxUniques = len(uniqueChars)
            maxWord = word
        }
    }
    return maxWord
}
```