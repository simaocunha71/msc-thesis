import (
    "regexp"
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
    // write your code here
    var count int
    var reg *regexp.Regexp
    reg, _ = regexp.Compile("I.*\\.\\s+")
    count = 0
    for _, value := range reg.FindAllStringIndex(S, -1) {
        count++
    }
    return count
}


