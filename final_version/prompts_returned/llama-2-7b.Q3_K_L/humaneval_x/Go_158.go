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
    sort.Strings(words)
    for i := range words {
        max := true
        for j, _ := range words[1:] {
            if words[i].Length() >= words[j+1].Length() {
                max = false
                break
            }
        }
        if !max {
            return words[i]
        }
    }
    return ""
}
