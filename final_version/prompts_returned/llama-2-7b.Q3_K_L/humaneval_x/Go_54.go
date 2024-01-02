
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

    // This is why I don't like using strings as a datatype.
    for _, r := range s0 {
        if !r.IsLetter() || !r.IsDigit() {
            return false
        }
    }
    for _, r := range s1 {
        if !r.IsLetter() || !r.IsDigit() {
            return false
        }
    }

    idx := 0
    char0, char1 := rune(s0[idx]), rune(s1[idx])
    // The check of IsLetter/IsDigit is not needed here (in case of
    // same character).
    for {
        if !char0.Equal(char1) {
            return false
        } else {
            idx++
            char0, char1 = rune(s0[idx]), rune(s1[idx])
        }
    }
}
