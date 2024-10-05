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
    var words []string
    if !strings.Contains(txt, " ") && !strings.Contains(txt, ",") {
        for i, v := range txt {
            if (i+1)%2 == 0 && v >= 'a' && v <= 'z' {
                words = append(words, string(v))
            }
        }
        return len(words)
    } else if strings.Contains(txt, ",") {
        words = strings.Split(txt, ",")
    } else {
        words = strings.Split(txt, " ")
    }
    return words
}
