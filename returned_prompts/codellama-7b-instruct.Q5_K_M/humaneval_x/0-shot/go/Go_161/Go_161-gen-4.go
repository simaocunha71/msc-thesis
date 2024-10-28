
	// We should check if the string contains any letter.
	// If not, we should reverse the string.
	// Then, we should return the reversed string.
	if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyz") {
		return reverseString(s)
	}

	// We should iterate over the string.
	// If we encounter a letter, we should reverse its case.
	// Otherwise, we should keep the character as it is.
	for i := 0; i < len(s); i++ {
		if isLetter(s[i]) {
			// We should reverse the letter's case.
			if isLower(s[i]) {
				s[i] = toUpper(s[i])
			} else {
				s[i] = toLower(s[i])
			}
		}
	}

	// We should return the resulted string.
	return s
}

// isLetter checks if the given character is a letter.
func isLetter(c byte) bool {
	return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z'
}

// isLower checks if the given character is a lowercase letter.
func isLower(c byte) bool {
	return c >= 'a' && c <= 'z'
}

// toLower converts the given character to lowercase.
func toLower(c byte) byte {
	return c - 'A' + 'a'
}

// toUpper converts the given character to uppercase.
func toUpper(c byte) byte {
	return c - 'a' + 'A'
}

// reverseString reverses the given string.
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(run