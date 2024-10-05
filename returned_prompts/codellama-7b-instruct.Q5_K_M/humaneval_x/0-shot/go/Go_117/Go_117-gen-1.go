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
    var result []string
    if s == "" {
        return result
    }

    words := strings.Fields(s)
    for _, word := range words {
        if isNConsonants(word, n) {
            result = append(result, word)
        }
    }
    return result
}

// isNConsonants checks if a word contains exactly n consonants.
func isNConsonants(word string, n int) bool {
    var count int
    for _, r := range word {
        if !isVowel(r) {
            count++
        }
        if count == n {
            return true
        }
    }
    return false
}

// isVowel checks if a rune is a vowel.
func isVowel(r rune) bool {
    switch r {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    }
    return false
}
