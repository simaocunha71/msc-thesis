
// Check if two words have the same characters.
// >>> SameChars('eabcdzzzz', 'dddzzzzzzzddeddabc')
// true
// >>> SameChars('abcd', 'dddddddabc')
// true
// >>> SameChars('dddddddabc', 'abcd')
// true
// >>> SameChars('eabcd', 'dddddddabc')
// false
// >>> SameChars('abcd', 'dddddddabce')
// false
// >>> SameChars('eabcdzzzz', 'dddzzzzzzzddddabc')
// false
func SameChars(s0 string, s1 string) bool {

	// Create two maps of the characters in the strings.
	s0Map := make(map[rune]int)
	s1Map := make(map[rune]int)

	// Count the characters in each string.
	for _, c := range s0 {
		s0Map[c]++
	}
	for _, c := range s1 {
		s1Map[c]++
	}

	// Compare the maps.
	for c, count := range s0Map {
		if s1Map[c] != count {
			return false
		}
	}
	return true
}
