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
    result = strings.Map(func(r rune) rune {
        if strings.ContainsRune(c,r) {
            return -1
        }
        return r
    }, s)
    return [2]interface{}{result,IsPalindrome(result)}
}

func IsPalindrome(s string) bool {
    return strings.ToLower(s) == strings.Reverse(strings.ToLower(s))
}

func Reverse(s string) string {
    return strings.Join(strings.Split(s,""),"")
}

func IsPalindrome(s string) bool {
    return strings.ToLower(s) == strings.ToLower(Reverse(s))
}

func ReverseDelete(s,c string) [2]interface{} {
    var result string
    var isPalindrome bool
    result,isPalindrome = reverseDelete(s,c)
    return [2]interface{}{result,isPalindrome}
}

func reverseDelete(s,c string) (string,bool) {
    result := strings.Map(func(r rune) rune {
        if strings.ContainsRune(c,r) {
            return -1
        }
        return r
    }, s)
    return result,isPalindrome(result)
}

func