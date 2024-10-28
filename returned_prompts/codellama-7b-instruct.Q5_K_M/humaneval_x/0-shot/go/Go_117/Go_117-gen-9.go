import (
    "bytes"
    "strings"
)

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
    words = strings.Fields(s)
    var consonants int
    var word string
    var i int
    for i = 0; i < len(words); i++ {
        consonants = 0
        word = words[i]
        for _, value := range word {
            if value == 'a' || value == 'e' || value == 'i' || value == 'o' || value == 'u' {
                continue
            } else {
                consonants += 1
            }
        }
        if consonants == n {
            return append(words, word)
        }
    }
    return words
}
