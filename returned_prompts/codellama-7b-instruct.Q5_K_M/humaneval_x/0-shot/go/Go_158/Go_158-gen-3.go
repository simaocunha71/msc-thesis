import (
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
func FindMax(words []string) string {

    var maxWord string
    var maxCharCount int

    for _, word := range words {
        charCount := make(map[rune]int)
        for _, char := range word {
            charCount[char]++
        }
        if maxCharCount < len(charCount) {
            maxCharCount = len(charCount)
            maxWord = word
        }
    }
    return maxWord
}

