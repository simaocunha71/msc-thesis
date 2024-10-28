
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
	return len(text) == 0 || text[0] == text[len(text)-1] && IsPalindrome(text[1:len(text)-1])
}
