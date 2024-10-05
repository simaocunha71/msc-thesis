Here is the Go function that solves the problem:

```go
import (
    "sort"
)

func FindMax(words []string) string {
    var maxWord string
    var maxUniqueChars int
    for _, word := range words {
        uniqueChars := len([]rune(uniqueCharsSet(word)))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        } else if uniqueChars == maxUniqueChars {
            if word < maxWord {
                maxWord = word
            }
        }
    }
    return maxWord
}

func uniqueCharsSet(word string) string {
    var set map[rune]bool
    for _, rune := range word {
        set[rune] = true
    }
    var result []rune
    for rune := range set {
        result = append(result, rune)
    }
    return string(result)
}
```

This function iterates over the list of words, calculates the number of unique characters in each word, and keeps track of the word with the maximum number of unique characters. If multiple words have the same maximum number of unique characters, it returns the one that comes first in lexicographical order. The helper function `uniqueCharsSet` is used to create a set of unique characters in a word. It uses a map to store the unique characters and then converts the map to a slice of runes. The slice of runes is then converted to a string. The `FindMax` function returns the word with the maximum number of unique characters. If multiple words have the same maximum number of unique characters, it returns the one that comes first in lexicographical order. 

The time complexity of this function is O(n*m) where n is the number of words and m is the maximum length of a word. The space complexity is O(m) for storing the set of unique characters in each word. 

The unit test for this function can be written as follows:

```go
func TestFindMax(t *testing.T) {
    testCases := []struct {
        input    []string
        expected string
    }{
        {[]string{"name", "of", "string"}, "string"},
        {[]string{"name", "enam", "game"}, "enam"},
        {[]string{"aaaaaaa", "bb", "cc"}, "aaaaaaa"},
    }
    for _, testCase := range testCases {
        if result := FindMax(testCase.input); result != testCase.expected