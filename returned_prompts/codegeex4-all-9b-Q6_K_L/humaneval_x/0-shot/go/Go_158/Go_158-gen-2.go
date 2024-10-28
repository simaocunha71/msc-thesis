Here is a possible implementation of the function in Go:

```go
func FindMax(words []string) string {
    maxUniqueCount := 0
    maxUniqueWord := ""

    for _, word := range words {
        uniqueCount := 0
        uniqueChars := make(map[rune]bool)

        for _, char := range word {
            if !uniqueChars[char] {
                uniqueChars[char] = true
                uniqueCount++
            }
        }

        if uniqueCount > maxUniqueCount || (uniqueCount == maxUniqueCount && word < maxUniqueWord) {
            maxUniqueCount = uniqueCount
            maxUniqueWord = word
        }
    }

    return maxUniqueWord
}
```

This function iterates over each word in the input list. For each word, it counts the number of unique characters by iterating over the characters in the word and checking if they have already been encountered. If a character is not in the `uniqueChars` map, it is added to the map and the `uniqueCount` is incremented. After counting the unique characters for a word, the function checks if the `uniqueCount` is greater than the current maximum `maxUniqueCount` or if it is equal to the `maxUniqueCount` but the word is lexicographically smaller than the current `maxUniqueWord`. If either of these conditions is met, the function updates `maxUniqueCount` and `maxUniqueWord`. Finally, the function returns the `maxUniqueWord` which has the maximum number of unique characters.