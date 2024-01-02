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
    words := make([]string, 0)
    for _, word := range strings.Split(s, " ") {
        if !strings.HasSuffix(word, ",") && !strings.HasPrefix(word, "!") && !strings.HasPrefix(word, "[") && !strings.HasPrefix(word, "{") && !strings.ContainsAny(word, "@#$%") {
            words = append(words, word)
        }
    }
    return words
}
