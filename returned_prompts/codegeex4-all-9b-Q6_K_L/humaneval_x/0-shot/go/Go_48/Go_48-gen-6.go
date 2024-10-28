package main

import "fmt"

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
    text = text + text
    text = Reverse(text)
    text = text[:len(text)/2]
    return text == Reverse(text)
}

func Reverse(text string) string {
    result := ""
    for _, c := range text {
        result = string(c) + result
    }
    return result
}

func main() {
    fmt.Println(IsPalindrome(""))
    fmt.Println(IsPalindrome("aba"))
    fmt.Println(IsPalindrome("aaaaa"))
    fmt.Println(IsPalindrome("zbcd"))
}
