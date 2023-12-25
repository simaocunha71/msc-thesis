
// Write a function that takes a string and returns true if the string
// length is a prime number or false otherwise
// Examples
// PrimeLength('Hello') == true
// PrimeLength('abcdcba') == true
// PrimeLength('kittens') == true
// PrimeLength('orange') == false
func PrimeLength(s string) bool {
	if s == "" || len(s) < 2 {
		return false // 1 or less
	} else if strings.ContainsAny(s, "13", "79") {
		return true
	} else {
		for i := 0; i < len(s)-1; i++ {
			for j := i + 2; j <= len(s); j++ {
				if s[i] == s[j-1] { // 1 or more, no duplicates allowed
					continue // Skip the current iteration if there is a match.
				} else {
					return false
				}
			}
			if s[i] == '0' || s[i] == '1' || s[i] == '2' || s[i] == '3' || s[i] == '4' || s[i] == '5' || s[i] == '6' || s[i] == '7' || s[i] == '8' {
				break // Stop the iteration when we find a number.
			} else if strings.HasPrefix(s, "0") || strings.ContainsAny(s, "0123456789abcdefghjkmnpqrstuwxyzABCDEFGHJKMNPRSTUWXYZ", 0) {
				break // Stop the iteration when we find a number or letter/string.
			} else if strings.HasPrefix(s, "1379") {
				return true // Stop the loop early as we found the string's length is a prime number before checking for duplicate numbers inside the string.
			} else {
				continue // Skip the