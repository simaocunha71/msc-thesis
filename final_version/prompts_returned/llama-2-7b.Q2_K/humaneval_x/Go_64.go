import (
    "strings"
)

// Write a function VowelsCount which takes a string representing
// a word as input and returns the number of vowels in the string.
// Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
// vowel, but only when it is at the end of the given word.
// 
// Example:
// >>> VowelsCount("abcde")
// 2
// >>> VowelsCount("ACEDY")
// 3
func VowelsCount(s string) int {
    v := make(map[rune]int, len(s))
    c := 0
    for _, r = range s {
        if strings.ContainsRune(c, r) || (r == 'y' && strings.HasSuffix(r, "e")) {
            v[r]++
        }
        c++
    }
    return int(len(v)) - 1
}