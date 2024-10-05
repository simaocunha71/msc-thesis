Here is a possible solution in Go:

```go
import (
    "sort"
    "strings"
)

func FindMax(words []string) string {
    sort.Strings(words)
    maxUniqueChars := 0
    maxWord := ""

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

    return maxWord
}
```

Here's how it works:

1. First we sort the input slice of strings in lexicographical order.
2. Then we initialize `maxUniqueChars` and `maxWord` to keep track of the maximum number of unique characters and the word that has them, respectively.
3. We iterate over the sorted slice of strings.
4. For each string, we create a map `uniqueChars` to keep track of unique characters in the string.
5. We iterate over each character in the string and add it to the map. If the character is already in the map, it will not be added again, ensuring that only unique characters are counted.
6. If the number of unique characters in the current string is greater than `maxUniqueChars`, we update `maxUniqueChars` and `maxWord`.
7. Finally, we return `maxWord`, which is the word with the maximum number of unique characters.

This solution has a time complexity of O(n*m*log(n)) where n is the number of words and m is the average length of the words. The space complexity is O(n) for the slice of strings and O(m) for the map of unique characters.