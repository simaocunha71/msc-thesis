    var res string
    for _, v := range s {
        if !strings.ContainsRune(c, v) {
            res += string(v)
        }
    }

    return [2]interface{}{res, isPalindrome(res)}
}

func isPalindrome(s string) bool {
    for i := 0; i < len(s)/2; i++ {
        if s[i] != s[len(s)-i-1] {
            return false
        }
    }
    return true
}

*/

package main

import (
	"fmt"
	"strings"
)

// Task
// We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
// then check if the result string is palindrome.
// A string is called palindrome if it reads the same backward as forward.
// You should return a tuple containing the result string and true/false for the check.
// Example
// For s = “abcde”, c “ae”, the result should be  (“bcd”,false)
// For s “abcdef”, c “b” , the result should be  (“acdef”,false)
// For s “abcdedcba”, c “ab”, the result should be  (“cdedc”,true)

func ReverseDelete(s, c string) (string, bool) {

	var res string
	for _, v := range s {
		if !strings.ContainsRune(c, v) {
			res += string(v)
		}
	}

	return res, isPalindrome(res)
}

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(ReverseDelete("abcde", "ae"))
	fmt.Println(ReverseDelete("abcdef",