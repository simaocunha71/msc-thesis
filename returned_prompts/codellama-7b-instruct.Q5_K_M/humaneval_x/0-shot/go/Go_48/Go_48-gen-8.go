
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
    for i, j := 0, len(text)-1; i < j; i, j = i+1, j-1 {
        if text[i] != text[j] {
            return false
        }
    }
    return true
}

