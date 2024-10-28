
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
    var reverse string
    for i := len(text) - 1; i >= 0; i-- {
        reverse = reverse + string(text[i])
    }
    return text == reverse
}

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
    var reverse string
    for i := len(text) - 1; i >= 0; i-- {
        reverse = reverse + string(text[i])
    }
    return text == reverse
}

