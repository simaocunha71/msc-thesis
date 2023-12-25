import (
    "strings"
)

// You are given a string representing a sentence,
// the sentence contains some words separated by a space,
// and you have to return a string that contains the words from the original sentence,
// whose lengths are prime numbers,
// the order of the words in the new string should be the same as the original one.
// 
// Example 1:
// Input: sentence = "This is a test"
// Output: "is"
// 
// Example 2:
// Input: sentence = "lets go for swimming"
// Output: "go for"
// 
// Constraints:
// * 1 <= len(sentence) <= 100
// * sentence contains only letters
func WordsInSentence(sentence string) string {
    words := strings.Split(sentence, " ")
    
    var wordsPairs string
    for _, word := range words {
        p := strings.Count(word[1:], "")
        if p == 2 && (strings.LastIndex(word, "e") < strings.LastIndex(word, "a")) {
            return "e" + strings.TrimPrefix(word, "e")
        } else if strings.IsAsciiCapitalized(word) {
            continue
        } else {
            wordsPairs += word + " "
        }
    }
    
    if len(wordsPairs) > 1 {
        return strings.TrimPrefix(wordsPairs, " ") + " "
    }
    
    return wordsPairs[0]
}