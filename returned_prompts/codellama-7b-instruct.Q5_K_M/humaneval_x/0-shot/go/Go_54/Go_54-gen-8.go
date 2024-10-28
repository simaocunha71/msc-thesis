
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
	for i, j := 0, 0; i < len(s0) && j < len(s1); {
		if s0[i] != s1[j] {
			return false
		}
		i++
		j++
	}
	return true
}
