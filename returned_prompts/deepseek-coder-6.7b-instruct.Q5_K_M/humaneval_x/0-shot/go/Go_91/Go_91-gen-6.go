    1. Create a slice to hold the words from the string.
    2. Split the string into words using the "regexp" package.
    3. Iterate over the slice to check if the word is starting with "I".
    4. If it is, increment a counter.
    5. Return the counter.

B:
    import(
        "strings"
    )
    
    func IsBored(S string) int {
        words := strings.Fields(S)
        counter := 0
        for _, word := range words {
            if strings.HasPrefix(word, "I") {
                counter++
            }
        }
        return counter
    }
}

// The function IsBored takes a string as an argument. The string contains
// sentences delimited by '.', '?' or '!' and the task is to count the
// number of sentences that start with the word "I".
func IsBored(s string) int {
	sentences := strings.FieldsFunc(s, func(c rune) bool {
		return c == '.' || c == '?' || c == '!'
	})
	count := 0
	for _, sentence := range sentences {
		if strings.HasPrefix(sentence, "I") {
			count++
		}
	}
	return count
}

// The function IsBored takes a string S as an argument. The string contains
// sentences delimited by '.', '?' or '!' and the task is to count the
// number of sentences that start with the word "I".
func IsBored(s string) int {
	re := regexp.MustCompile("[.?!]")
	sentences := re.Split(s, -1)
	count := 0
	for _, sentence := range sentences {
		trimmed := strings.TrimSpace(sentence)
		if strings.HasPrefix(trimmed, "I") {
			count++
		}
	}
	return count
}
*/

// Test cases
// IsBored("Hello world") -> 0
// IsBored("The sky is blue. The sun is shining. I love this weather") -> 1
