Here is the solution:
```go
package main

import (
    "strings"
)

// Test if given string is a palindrome.
func IsPalindrome(str string) bool {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result) == str
}

// Find the shortest palindrome that begins with a supplied string.
// Algorithm idea is simple:
// - Find the longest postfix of supplied string that is a palindrome.
// - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
// >>> MakePalindrome('')
// ''
// >>> MakePalindrome('cat')
// 'catac'
// >>> MakePalindrome('cata')
// 'catac'
func MakePalindrome(str string) string {
    // Find the longest postfix of supplied string that is a palindrome.
    for i := len(str); i > 0; i-- {
        postfix := str[len(str)-i:]
        if IsPalindrome(postfix) {
            // Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
            return str + reverse(str[:len(str)-i])
        }
    }
    return str
}

func reverse(str string) string {
    runes := []rune(str)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}

func main() {
    println(MakePalindrome(""))  // ''
    println(MakePalindrome("cat"))  // 'catac'
    println(MakePalindrome("cata"))  // 'catac'
}
```
This solution finds the longest postfix of the supplied string that is a palindrome. It then appends the reverse of the string prefix that comes before the palindromic suffix to the end of the string. This ensures that the resulting string is the shortest palindrome that begins with the supplied string. The `IsPalindrome` function is used to check if a string is a palindrome, and the `reverse` function is used to reverse a string. The `MakePalindrome` function returns the shortest palindrome that begins with the supplied string. In the `main` function, we test the `MakePalindrome`