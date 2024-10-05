Here is the solution in Go:
```go
import (
    "strings"
)

func ReverseDelete(s, c string) [2]interface{} {
    // Create a new string by deleting all characters in s that are equal to any character in c
    newS := ""
    for _, char := range s {
        if !strings.Contains(c, string(char)) {
            newS += string(char)
        }
    }
    
    // Check if the new string is palindrome
    isPalindrome := false
    if strings.ToLower(newS) == strings.ReverseString(strings.ToLower(newS)) {
        isPalindrome = true
    }
    
    // Return the result
    return [2]interface{}{newS, isPalindrome}
}

// ReverseString returns the reverse of the input string
func ReverseString(s string) string {
    runes := []rune(s)
    reverse := []rune{}
    for i := len(runes) - 1; i >= 0; i-- {
        reverse = append(reverse, runes[i])
    }
    return string(reverse)
}
```
This solution first creates a new string `newS` by deleting all characters in `s` that are equal to any character in `c`. Then it checks if the new string is palindrome by comparing it with its reverse. If it is palindrome, it returns a tuple containing the new string and `true`; otherwise, it returns a tuple containing the new string and `false`. The `ReverseString` function is used to reverse the input string. Note that this solution assumes that the input strings only contain ASCII characters. If the input strings can contain non-ASCII characters, you may need to use a more complex solution.