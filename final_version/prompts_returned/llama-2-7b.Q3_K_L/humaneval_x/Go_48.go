
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
    if text == "" {
        return true
    }
    i := 0; j:= len(text)-1
    for ;i < j; i++, j--{
        if !(text[i] == text[j]) {
            return false
        }
    }
    return true
}
