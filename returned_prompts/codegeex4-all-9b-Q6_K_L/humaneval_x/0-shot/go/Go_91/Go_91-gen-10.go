```go
package main

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
	// Create a regular expression to match sentences starting with "I"
	re := regexp.MustCompile(`(?i)^[^a-z]*i[^a-z]*\.|[^a-z]*i[^a-z]*\?|[^a-z]*i[^a-z]*!`)

	// Find all matches and count them
	return len(re.FindAllString(S, -1))
}

func main() {
	// Test cases
	println(IsBored("Hello world")) // 0
	println(IsBored("The sky is blue. The sun is shining. I love this weather")) // 1
}
```