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
    words := strings.Fields(txt)
    if len(words) > 0 {
        return words
    }
    if strings.Contains(txt, ",") {
        words = strings.Split(txt, ",")
        if len(words) > 0 {
            return words
        }
    }
    count := 0
    for _, v := range txt {
        if v >= 'a' && v <= 'z' && (int(v)-int('a'))&1 == 1 {
            count++
        }
    }
    return count
}
