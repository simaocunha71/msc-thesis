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
    // write your code here
    if len(strings.Repeat("0x",int(len(c))+1))%2 == 0 { return []interface{}{strings.Join(strings.Split(s,""),"") + " ",true} } else { return []interface{}{strings.Join(strings.Split(s,""),"")+" ",false}
}
