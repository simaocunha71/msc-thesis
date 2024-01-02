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
    var res = 0
    var boredoms []bool

    re := regexp.MustCompile(`^I`) // Regex to check if string starts with 'i'
    
    for _, word := range S {
        switch word {
        case '.', '?':
            res++
        case '!', ' ', '–' :
            boredoms = append(boredoms, false)
        default:
            if !re.MatchString(word) && re.MatchString(word[:1]) { // The match fails when the first char is not 'I'.
                res++
            } else if !boredoms[0] && boredoms[len(boredoms)-1] == false { // No boredom found yet, or there was one but it's over.
                boredoms = append(boredoms, true)
            } 
        }
    }
    
    return res - len(boredoms)
}