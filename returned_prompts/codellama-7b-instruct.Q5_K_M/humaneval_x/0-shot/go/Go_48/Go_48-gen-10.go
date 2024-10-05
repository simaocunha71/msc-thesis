
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

	text = strings.ToLower(text)
	length := len(text)
	for i := 0; i < length/2; i++ {
		if text[i] != text[length-i-1] {
			return false
		}
	}
	return true
}
