import (
    "bufio"
    "os"
    "regexp"
    "strconv"
    "strings"
)

// You'll be given a string of words, and your task is to count the number
// of boredoms. A boredom is a sentence that starts with the word "I".
// Sentences are delimited by '.', '?' or '!'.
// 
// For example:
// >>> IsBored("Hello world")
// 0
// >>> IsBored("The sky is blue. The sun is shining. I love this weather")
// 1
func IsBored(S string) int {

    // Your code here

    // 1. First, we'll get the number of words in the string
    // 2. Then, we'll loop through them and check if they're boredoms
    // 3. We'll keep a counter of how many boredoms we find

    // 1. First, we'll get the number of words in the string
    // 1.1. We'll split the string into an array of words
    // 1.2. We'll get the length of that array
    words := strings.Split(S, " ")
    n := len(words)

    // 2. Then, we'll loop through them and check if they're boredoms
    // 2.1. We'll get the current word
    // 2.2. We'll check if it starts with the word "I"
    // 2.3. If it does, we'll increment the boredom counter
    boredomCount := 0
    for i := 0; i < n; i++ {
        currentWord := words[i]
        if strings.HasPrefix(currentWord, "I") {
            boredomCount++
        }
    }

    // 3. We'll return the boredom count
    return boredomCount
}

