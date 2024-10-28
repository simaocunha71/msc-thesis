
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

	var left, right int
	for left < len(text) && right > -1 {
		if text[left] == text[right] {
			left++
			right--
		} else {
			return false
		}
	}

	return true
}
