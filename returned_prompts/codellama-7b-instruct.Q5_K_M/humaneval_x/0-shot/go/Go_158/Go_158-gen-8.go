import (
    "sort"
)

// Write a function that accepts a list of strings.
// The list contains different words. Return the word with maximum number
// of unique characters. If multiple strings have maximum number of unique
// characters, return the one which comes first in lexicographical order.
// 
// FindMax(["name", "of", "string"]) == "string"
// FindMax(["name", "enam", "game"]) == "enam"
// FindMax(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
func FindMax(words []string) string {

    if len(words) == 0 {
        return ""
    }

    sort.Strings(words)

    max := 0
    var ret string
    for _, word := range words {
        if len(word) > max {
            max = len(word)
            ret = word
        }
    }

    return ret
}
