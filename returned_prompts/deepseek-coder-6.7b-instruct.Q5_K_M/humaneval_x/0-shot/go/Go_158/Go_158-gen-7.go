    sort.Strings(words)

B:
    maxWord := ""
    maxCount := 0

C:
    for _, word := range words {
        count := 0
        charMap := make(map[rune]bool)
        for _, char := range word {
            if _, ok := charMap[char]; !ok {
                charMap[char] = true
                count++
            }
        }
        if count > maxCount {
            maxCount = count
            maxWord = word
        }
    }

    return maxWord
}
```

## Solution

```go
import  (
    "sort"
)

// Write a function that accepts a list of strings.
// The list contains different words. Return the word with maximum number
// of unique characters. If multiple strings have maximum number of unique
// characters, return the one which comes first in lexicographical order.
// 
// FindMax(["name", "of", "string"]) == "string"
// FindMax(["name", "enam", "game"]) == "enam"
// FindMax(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
func FindMax(words  []string) string  {

    // Sort the words in lexicographical order
    sort.Strings(words)

    // Initialize variables to store the word with the maximum number of unique characters
    // and the maximum count of unique characters
    maxWord := ""
    maxCount := 0

    // Iterate over each word in the list
    for _, word := range words {
        count := 0
        charMap := make(map[rune]bool)
        // Iterate over each character in the word
        for _, char := range word {
            // If the character is not in the map, add it to the map and increment the count
            if _, ok := charMap[char]; !ok {
                charMap[char] = true
                count++
            }
        }
        // If the count of unique characters in the current word is greater than the maximum count,
        // update the maximum count and the word
       