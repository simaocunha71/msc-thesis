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

    // Write your code here
    // Find the length of the longest string
    maxLen := 0
    for _, word := range words {
        if len(word) > maxLen {
            maxLen = len(word)
        }
    }
    
    // Find the longest word
    longestWord := ""
    for _, word := range words {
        if len(word) == maxLen {
            longestWord = word
            break
        }
    }
    
    // Find the word with the maximum number of unique characters
    maxUnique := 0
    for _, char := range longestWord {
        uniqueChar := ""
        for _, word := range words {
            if strings.Contains(word, string(char)) {
                uniqueChar += string(char)
            }
        }
        if len(uniqueChar) > maxUnique {
            maxUnique = len(uniqueChar)
        }
    }
    
    // Return the word with the maximum number of unique characters
    for _, word := range words {
        if len(word) == maxLen && len(word) == maxUnique {
            return word
        }
    }
    
    // Return the word with the maximum number of unique characters
    for _, word := range words {
        if len(word) == maxLen && len(word) == maxUnique {
            return word
        }
    }
    
    // If there are multiple words with the maximum number of unique characters,
    // return the first word in the list
    return longestWord
}
