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
    type tuple struct {
        word string
        unique int
    }
    tuples := make([]tuple, len(words))
    for i, word := range words {
        tuples[i] = tuple{word, len(make(map[rune]struct{}, 0).(map[rune]struct{}))}
        for _, ch := range word {
            tuples[i].unique += 1
            tuples[i].word = word
        }
    }
    sort.Slice(tuples, func(i, j int) bool {
        if tuples[i].unique > tuples[j].unique {
            return true
        } else if tuples[i].unique < tuples[j].unique {
            return false
        } else {
            return tuples[i].word < tuples[j].word
        }
    })
    return tuples[len(tuples)-1].word
}
