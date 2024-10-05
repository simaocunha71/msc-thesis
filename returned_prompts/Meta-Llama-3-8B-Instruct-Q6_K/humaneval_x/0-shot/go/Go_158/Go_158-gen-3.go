Here is a Go function that solves the problem:

```go
import (
    "sort"
)

func FindMax(words []string) string {
    maxWord := ""
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUniqueChars {
            maxUniqueChars = len(uniqueChars)
            maxWord = word
        } else if len(uniqueChars) == maxUniqueChars {
            if word < maxWord {
                maxWord = word
            }
        }
    }
    return maxWord
}
```

This function iterates over each word in the input list. For each word, it counts the number of unique characters using a map. If the number of unique characters in the current word is greater than the maximum number of unique characters found so far, it updates the maximum number of unique characters and the maximum word. If the number of unique characters in the current word is equal to the maximum number of unique characters found so far, it checks if the current word is lexicographically smaller than the maximum word and updates the maximum word if necessary. Finally, it returns the maximum word.

The time complexity of this function is O(n*m), where n is the number of words and m is the maximum length of a word. The space complexity is O(m), where m is the maximum length of a word. This is because we are using a map to count the unique characters in each word, and the size of the map is proportional to the length of the word. We are also storing the maximum word, which can be up to m characters long. Therefore, the space complexity is linear in the maximum length of a word. 