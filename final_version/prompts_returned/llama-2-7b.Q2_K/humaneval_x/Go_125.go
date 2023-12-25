import (
    "strings"
)

// Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
// should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
// alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
// Examples
// SplitWords("Hello world!") ➞ ["Hello", "world!"]
// SplitWords("Hello,world!") ➞ ["Hello", "world!"]
// SplitWords("abcdef") == 3
func SplitWords(txt string) interface{} {
    // split words into an array of strings
    words := make([]string, 0)
    for _, c := range txt {
        switch c {
            case 'a':
                if ord('b') > ord('z'):
                    words = append(words, c.ToString())
                break
            case ',':
                if ord(',') <= ord('z'): // commas are only split on the last word
                    words = append(words, txt[txt.IndexOf(','):])
        }
    }
    return words
}
