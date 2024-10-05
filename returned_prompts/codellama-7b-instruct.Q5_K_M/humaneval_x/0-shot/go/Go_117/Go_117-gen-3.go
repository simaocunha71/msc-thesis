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
    if s == "" {
        return []string{}
    }

    var words []string
    var word bytes.Buffer
    for i, r := range s {
        if !isLetter(r) {
            if word.Len() == n {
                words = append(words, word.String())
            }
            word.Reset()
        } else if isConsonant(r) {
            word.WriteRune(r)
        }
        if i > 0 && !isLetter(rune(s[i-1])) && word.Len() == n {
            words = append(words, word.String())
            word.Reset()
        }
    }
    return words
}

// isLetter returns true if the rune is a letter.
func isLetter(r rune) bool {
    return 'A' <= r && r <= 'Z' || 'a' <= r && r <= 'z'
}

// isConsonant returns true if the rune is a consonant.
func isConsonant(r rune) bool {
    return 'A' <= r && r <= 'Z' && r != 'A' && r != 'E' && r != 'I' && r != 'O'