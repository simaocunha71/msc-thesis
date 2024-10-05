Here is a Go solution for the problem:

```go
func FindMax(words []string) string {
    maxUnique := 0
    maxWord := ""
    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUnique || (len(uniqueChars) == maxUnique && word < maxWord) {
            maxUnique = len(uniqueChars)
            maxWord = word
        }
    }
    return maxWord
}
```

This function iterates over the list of strings. For each string, it counts the number of unique characters by using a map to track them. If the current string has more unique characters than the previously stored maximum, or if it has the same number of unique characters but comes lexicographically first, the function updates the maximum and the corresponding string. At the end, it returns the string with the maximum number of unique characters.