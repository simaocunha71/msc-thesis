import (
    "strings"
)

// You will be given a string of words separated by commas or spaces. Your task is
// to split the string into words and return an array of the words.
// 
// For example:
// WordsString("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
// WordsString("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
func WordsString(s string) []string {
    words := make([]string, 0, len(s))
    
    for idx, str := range s {
        if strings.ContainsRune(str, ',') || str == "\n" {
            splitAt(idx + 1, s, words)
        } else {
            words = append(words, str)
        }
    }
    
    return words
}