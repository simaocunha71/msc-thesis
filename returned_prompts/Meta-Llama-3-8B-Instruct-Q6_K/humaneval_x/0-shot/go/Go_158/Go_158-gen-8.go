Here is the solution in Go:
```go
import (
    "sort"
)

func FindMax(words []string) string {
    var maxWord string
    var maxUniqueChars int
    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUniqueChars {
            maxUniqueChars = len(uniqueChars)
            maxWord = word
        }
    }
    sort.Strings(words)
    for _, word := range words {
        if len(uniqueCharsFromWord(word)) > maxUniqueChars {
            maxUniqueChars = len(uniqueCharsFromWord(word))
            maxWord = word
        }
    }
    return maxWord
}

func uniqueCharsFromWord(word string) map[rune]bool {
    uniqueChars := make(map[rune]bool)
    for _, char := range word {
        uniqueChars[char] = true
    }
    return uniqueChars
}
```
The function `FindMax` iterates over each word in the input list. For each word, it creates a map of unique characters and checks if the length of this map is greater than the maximum unique characters found so far. If it is, it updates the maximum unique characters and the corresponding word.

After that, it sorts the list of words in lexicographical order. Then it iterates over the sorted list again, and for each word, it checks if the length of its unique characters is greater than the maximum unique characters found so far. If it is, it updates the maximum unique characters and the corresponding word.

Finally, it returns the word with the maximum number of unique characters. If multiple words have the same maximum number of unique characters, it returns the one which comes first in lexicographical order.

The function `uniqueCharsFromWord` is a helper function that creates a map of unique characters for a given word. It is used by the `FindMax` function to calculate the number of unique characters in each word.