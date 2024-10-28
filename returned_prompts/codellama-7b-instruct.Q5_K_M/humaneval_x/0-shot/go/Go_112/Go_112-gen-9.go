import (
    "strings"
)

// Task
// We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
// then check if the result string is palindrome.
// A string is called palindrome if it reads the same backward as forward.
// You should return a tuple containing the result string and true/false for the check.
// Example
// For s = "abcde", c = "ae", the result should be ('bcd',false)
// For s = "abcdef", c = "b"  the result should be ('acdef',false)
// For s = "abcdedcba", c = "ab", the result should be ('cdedc',true)
func ReverseDelete(s,c string) [2]interface{} {
    var result string
    var isPalindrome bool
    for _, sChar := range s {
        if !strings.Contains(c, string(sChar)) {
            result += string(sChar)
        }
    }
    isPalindrome = result == strings.Reverse(result)
    return [2]interface{}{result, isPalindrome}
}
