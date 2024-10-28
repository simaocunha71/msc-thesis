import (
    "sort"
    "strings"
)

// Write a function that takes a string and returns an ordered version of it.
// Ordered version of string, is a string where all words (separated by space)
// are replaced by a new word where all the characters arranged in
// ascending order based on ascii value.
// Note: You should keep the order of words and blank spaces in the sentence.
// 
// For example:
// AntiShuffle('Hi') returns 'Hi'
// AntiShuffle('hello') returns 'ehllo'
// AntiShuffle('Hello World!!!') returns 'Hello !!!Wdlor'
func AntiShuffle(s string) string {

    // split the string into words
    words := strings.Fields(s)
    // sort the words
    sort.Strings(words)
    // join the sorted words
    return strings.Join(words, " ")
}


