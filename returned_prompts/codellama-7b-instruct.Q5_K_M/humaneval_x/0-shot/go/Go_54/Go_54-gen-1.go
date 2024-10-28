
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

	if len(s0) != len(s1) {
		return false
	}
	var count int
	for i, c := range s0 {
		if c == s1[i] {
			count++
		}
	}
	if count == len(s0) {
		return true
	}
	return false
}
