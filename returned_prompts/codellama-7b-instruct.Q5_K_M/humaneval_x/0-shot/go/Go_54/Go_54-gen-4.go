
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

	m := make(map[byte]bool)
	for _, b := range s0 {
		m[b] = true
	}
	for _, b := range s1 {
		if _, ok := m[b]; !ok {
			return false
		}
	}
	return true
}

