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

    // Write your code here
    type wordInfo struct {
        word string
        uniqueCharCount int
    }
    
    var wordInfoList []wordInfo
    
    for _, word := range words {
        uniqueCharCount := 0
        for _, char := range word {
            if !strings.Contains(word, string(char)) {
                uniqueCharCount++
            }
        }
        wordInfoList = append(wordInfoList, wordInfo{word, uniqueCharCount})
    }
    
    sort.Slice(wordInfoList, func(i, j int) bool {
        if wordInfoList[i].uniqueCharCount > wordInfoList[j].uniqueCharCount {
            return true
        } else if wordInfoList[i].uniqueCharCount < wordInfoList[j].uniqueCharCount {
            return false
        } else {
            return wordInfoList[i].word < wordInfoList[j].word
        }
    })
    
    return wordInfoList[0].word
}
