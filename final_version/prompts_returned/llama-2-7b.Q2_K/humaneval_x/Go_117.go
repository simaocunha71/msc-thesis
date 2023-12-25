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
    res := make([]string, 0, len(s))
    if s == "" {
        return append(res, "")
    }
    for i := range []rune(s) {
        r := rune(i)
        if !isConsonant(r) && (n == 1 || n == 2) && strings.ContainsAny(rune(0), 'h', 'w') {
            continue
        } else if isVowel(r) {
            break
        }
    }
    return append(res, []string{}...)
}
