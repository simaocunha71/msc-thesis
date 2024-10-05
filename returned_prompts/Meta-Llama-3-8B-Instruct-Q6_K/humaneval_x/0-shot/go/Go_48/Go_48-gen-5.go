```go
package main
import "strings"

func IsPalindrome(text string) bool {
    text = strings.ToLower(text)
    for i := 0; i < len(text)/2; i++ {
        if text[i] != text[len(text)-1-i] {
            return false
        }
    }
    return true
}
```


Explanation:
The function `IsPalindrome` checks if the given string is a palindrome. It converts the string to lowercase using the `strings.ToLower` function to make the comparison case-insensitive. Then, it iterates over the first half of the string, comparing each character with the corresponding character from the end of the string. If it finds a mismatch, it returns `false`. If it finishes the iteration without finding a mismatch, it returns `true`. This approach ensures that the function works correctly even for strings with non-alphanumeric characters, such as spaces and punctuation.

Note: The function does not handle non-ASCII characters. If you need to handle non-ASCII characters, you would need to use a more complex approach, such as using Unicode code points or a regular expression.