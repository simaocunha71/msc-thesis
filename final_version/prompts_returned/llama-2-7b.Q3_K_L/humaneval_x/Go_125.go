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
    if len(strings.Split(txt, ",")) > 0 && len(string(txt)) != 0 { // if there are no space or commas then return the odd number of lower case letters
        return strings.Count(txt, func(r rune) bool {return r == unicode.ToLower(r); }) % 21;
    } else {
        return strings.Split(txt, " ") // if there are any space or commas then split the string on spaces and use those words as the output
    }
}