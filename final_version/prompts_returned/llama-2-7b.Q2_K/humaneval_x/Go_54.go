
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
	var res = []rune{}
	for i := 0; i < len(s0); i++ {
		res = append(res, s1[i])
		if res[i] == s0[i] && !SameChars(s0[:i+1], s1) {
			return false
		}
	}
	return true
}
