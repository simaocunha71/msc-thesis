Here is a Go function that implements the described behavior:

```go
import (
    "sort"
)

func FindMax(words []string) string {
    max := ""
    maxCount := 0
    for _, word := range words {
        count := len(make(map[rune]bool)(strings.Map(func(r rune) rune {
            if !strings.Contains("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", string(r)) {
                return -1
            }
            return r
        }, strings.ToLower(word)))))
        if count > maxCount {
            maxCount = count
            max = word
        } else if count == maxCount {
            if strings.Compare(word, max) < 0 {
                max = word
            }
        }
    }
    return max
}
```
The function iterates over each word in the input list. For each word, it calculates the count of unique characters. The count of unique characters is calculated by converting the word to lowercase, creating a map of the characters, and then returning the length of the map. This is done to ensure that the count is case-insensitive.

The function then compares the count of the current word with the maximum count found so far. If the count is greater, it updates the maximum count and the maximum word. If the count is equal to the maximum count, it compares the words lexicographically and updates the maximum word if the current word is lexicographically smaller.

Finally, the function returns the maximum word. If no words are found, it returns an empty string. The function is case-insensitive, meaning that it treats uppercase and lowercase letters as the same. It also does not count non-alphabetic characters.