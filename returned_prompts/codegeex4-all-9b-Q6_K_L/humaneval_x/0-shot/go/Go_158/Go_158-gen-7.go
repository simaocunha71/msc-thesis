Here is a possible implementation of the `FindMax` function:

```go
func FindMax(words []string) string {
    maxWord := ""
    maxUniqueChars := 0

    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }

        if len(uniqueChars) > maxUniqueChars || (len(uniqueChars) == maxUniqueChars && word < maxWord) {
            maxUniqueChars = len(uniqueChars)
            maxWord = word
        }
    }

    return maxWord
}
```

This implementation iterates over each word in the input list. For each word, it creates a map to keep track of the unique characters in the word. It then checks if the current word has more unique characters than the previous maximum, or if it has the same number of unique characters but comes earlier in lexicographical order. If either of these conditions is true, it updates the maximum number of unique characters and the maximum word.

Finally, it returns the maximum word.