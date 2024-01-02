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
    // Solution #1: O(n^2) space O(m * n) time
    //         O(m * m) O(n) to get the words in s.
    //         O(m * n) for the selection algorithm (O(m+n)).
    res := make([]string, 0, len(s))
    for _, c := range strings.Split(s, "") {
        if n == 0 {
            continue
        }
        if n < 1 || c == "" {
            break
        }

        words := selectWords(c, n-1)
        res = append(res, words...)
    }
    return res
}

func selectWords(s string, n int) []string {
    // Solution #2: O(n^2) space O(m * k) time, where m is the length of s and k is the number of letters in word.
    words := make([]string, 0, len(s))
    for i, c := range strings.Split(s, "") {
        if n == 0 {
            break
        }
        if _, ok := letterWordSets[c]; !ok {
            continue
        }

        letWordCount := len(s