
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
    if text == "" || len(text) < 2 {
        return false
    } else {
	    for i := 0; ; i++ {
            left, right := i, i+1
            if i >= len(text)-1 {
                break
            }
            for j := 0; j <= i && text[i] != "" || j < len(text); j++ {
                switch text[j] {
                    case 'a': fallthrough
                    case 'b': fallthrough
                    case 'c', 'd': fallthrough
                    case 'e': fallthrough
                    case 'f', 'g': fallthrough
                    case 'h': fallthrough
                    case 'i': fallthrough
                    case 'j': fallthrough
                    case 'k': fallthrough
                    case 'l': fallthrough
                    case 'm': fallthrough
                    case 'n': fallthrough
                    case 'o', 'p': fallthrough
                    case 'q': fallthrough
                    case 'r': fallthrough
                    case 's': fallthrough
                    case 't': fallthrough
                    case 'u': fallthrough
                    case 'v': fallthrough
                    case 'w', 'x': fallthrough
                    case 'y': fallthrough
                    case 'z': fallthrough
                }
            }
        }
        return text[0:i] == text[len(text)-1-:i]
    }
}
