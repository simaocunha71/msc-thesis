```go
func FindMax(words []string) string {
    // Create a map to store the count of unique characters in each word
    uniqueCount := make(map[string]int)
    
    // Iterate over the words and count the unique characters in each word
    for _, word := range words {
        uniqueSet := make(map[rune]bool)
        for _, char := range word {
            uniqueSet[char] = true
        }
        uniqueCount[word] = len(uniqueSet)
    }
    
    // Find the word with maximum number of unique characters
    maxUniqueWord := ""
    maxUniqueCount := 0
    for word, count := range uniqueCount {
        if count > maxUniqueCount {
            maxUniqueWord = word
            maxUniqueCount = count
        } else if count == maxUniqueCount && word < maxUniqueWord {
            maxUniqueWord = word
        }
    }
    
    return maxUniqueWord
}
```