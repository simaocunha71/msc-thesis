Here is a Go solution for the problem:

```go
import (
    "sort"
)

func FindMax(words []string) string {
    var maxUnique int
    var result string

    for _, word := range words {
        unique := len([]rune(uniqueChars(word)))
        if unique > maxUnique {
            maxUnique = unique
            result = word
        } else if unique == maxUnique {
            if word < result {
                result = word
            }
        }
    }

    return result
}

func uniqueChars(s string) string {
    chars := make(map[rune]bool)
    var sb strings.Builder

    for _, char := range []rune(s) {
        if !chars[char] {
            chars[char] = true
            sb.WriteString(string(char))
        }
    }

    return sb.String()
}
```

In this solution, we iterate over each word in the input list. For each word, we calculate the number of unique characters using the `uniqueChars` function. We then compare this number with the current maximum. If it's greater, we update the maximum and the result word. If it's equal, we compare the words lexicographically to choose the one that comes first.

The `uniqueChars` function uses a map to keep track of unique characters and a strings.Builder to build the result string. It iterates over the input string, adding each character to the map and the result string if it's not already present in the map. The result string contains all the unique characters in the input string. 

This solution has a time complexity of O(n*m) where n is the number of words and m is the maximum length of a word, because we're iterating over each word and each character in the words. The space complexity is O(n*m) as well, because we're storing the unique characters and the result string. 

Note: This solution assumes that the input list contains at least one word. If the list can be empty, you should add a check for that case.  Also, the solution assumes that the input words are in lowercase. If the words can be in any case, you should convert them to lowercase before processing.  Finally, the solution assumes that the input words contain only ASCII characters. If the words can contain non-ASCII characters, you should use a more complex function to calculate the unique characters.  For example, you could use a map to keep track of unique runes, or you could use a set to keep track of unique