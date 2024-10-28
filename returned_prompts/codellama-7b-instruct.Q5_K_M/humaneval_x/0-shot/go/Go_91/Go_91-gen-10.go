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
    var re = regexp.MustCompile(`\bI\b`)
    var count = 0
    for _, sentence := range strings.Split(S, ".") {
        for _, word := range strings.Split(sentence, " ") {
            if re.MatchString(word) {
                count++
            }
        }
    }
    return count
}

func IsBored(s string) int {
	re := regexp.MustCompile(`\bI\b`)
	var count int
	for _, sentence := range strings.Split(s, ".") {
		if re.MatchString(sentence) {
			count++
		}
	}
	return count
}

func IsBored(s string) int {
	return len(regexp.MustCompile(`\bI\b`).FindAllString(s, -1))
}

func IsBored(s string) int {
	return len(regexp.MustCompile(`\bI\b`).FindAllString(s, -1))
}

func IsBored(s string) int {
	return len(regexp.MustCompile(`\bI\b`).FindAllString(s, -1))
}
