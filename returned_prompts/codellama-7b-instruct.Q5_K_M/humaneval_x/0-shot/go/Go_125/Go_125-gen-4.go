import (
    "regexp"
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

    var split = regexp.MustCompile(`\s+`)
    var splitComma = regexp.MustCompile(`,\s+`)

    if split.MatchString(txt) {
        return strings.Split(txt, " ")
    }

    if splitComma.MatchString(txt) {
        return strings.Split(txt, ", ")
    }

    var letters = []rune(txt)
    var odd = 0
    for i, letter := range letters {
        if letter >= 'a' && letter <= 'z' {
            if i%2 != 0 {
                odd++
            }
        }
    }
    return odd
}
