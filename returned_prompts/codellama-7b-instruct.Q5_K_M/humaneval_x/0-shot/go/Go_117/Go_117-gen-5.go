import (
    "bytes"
    "strings"
)

func SelectWords(s string, n int) []string {
    var words []string
    var word string
    for _, c := range s {
        if c == ' ' {
            if len(word) == n {
                words = append(words, word)
            }
            word = ""
        } else {
            word += string(c)
        }
    }
    if len(word) == n {
        words = append(words, word)
    }
    return words
}

// Given a string s and a natural number n, you have been tasked to implement
// a function that returns a list of all words from string s that contain exactly
// n consonants, in order these words appear in the string s.
// If the string s is empty then the function should return an empty list.
// Note: you may assume the input string contains only letters and spaces.
// Examples:
// SelectWords("Mary had a little lamb", 4) ==> ["little"]
// SelectWords("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
// SelectWords("simple white space", 2) ==> []
// SelectWords("Hello world", 4) ==> ["world"]
// SelectWords("Uncle sam", 3) ==> ["Uncle"]
func SelectWords(s string, n int) []string {
    var words []string
    for _, word := range strings.Fields(s) {
        if len(word) == n {
            words = append(words, word)
        }
    }
    return words
}
