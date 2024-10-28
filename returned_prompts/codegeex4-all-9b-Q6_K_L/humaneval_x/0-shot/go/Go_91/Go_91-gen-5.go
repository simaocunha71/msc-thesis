```go
package main

import (
	"strings"
	"regexp"
)

func IsBored(S string) int {
	// Split the input string into sentences
	sentences := strings.Split(S, `\.|\?|!`)
	// Initialize the boredom counter
	boredom := 0
	// Iterate over the sentences
	for _, sentence := range sentences {
		// Check if the sentence starts with "I"
		if strings.HasPrefix(strings.TrimSpace(sentence), "I") {
			// Increment the boredom counter
			boredom++
		}
	}
	// Return the boredom count
	return boredom
}

func main() {
	// Test cases
	println(IsBored("Hello world")) // Expected: 0
	println(IsBored("The sky is blue. The sun is shining. I love this weather")) // Expected: 1
}
```
