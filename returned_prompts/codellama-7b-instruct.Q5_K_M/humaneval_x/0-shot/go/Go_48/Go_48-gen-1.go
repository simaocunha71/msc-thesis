
// Checks if given string is a palindrome
// >>> IsPalindrome('')
// true
// >>> IsPalindrome('aba')
// true
// >>> IsPalindrome('aaaaa')
// true
// >>> IsPalindrome('zbcd')
// false
func IsPalindrome(text string) bool {
	if len(text) == 0 {
		return true
	}
	for i := 0; i < len(text); i++ {
		if text[i] != text[len(text)-i-1] {
			return false
		}
	}
	return true
}
