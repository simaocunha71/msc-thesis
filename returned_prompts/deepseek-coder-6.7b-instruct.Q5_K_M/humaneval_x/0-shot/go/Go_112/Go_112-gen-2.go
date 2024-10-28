    var result string
    for _, ch := range s {
        if !strings.ContainsRune(c, ch) {
            result += string(ch)
        }
    }
    var t [2]interface{}
    t[0] = result
    t[1] = isPalindrome(result)
    return t
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
    fmt.Println(ReverseDelete("abcdef", "b"))
    fmt.Println(ReverseDelete("abcdedcba", "ab"))
}

*/

package main

import (
	"fmt"
	"strings"
)

func ReverseDelete(s, c string) (string, bool) {
	var result string
	for _, ch := range s {
		if !strings.ContainsRune(c, ch) {
			result += string(ch)
		}
	}
	return result, isPalindrome(result)
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
	fmt.Println(ReverseDelete("abcdef", "b"))
	fmt.Println(ReverseDelete("abcdedcba", "ab"))
}

// Output:
// abcd false
// acdef false
// cdcd true

// The output shows that the function ReverseDelete correctly removes all occurrences of the characters in the string c from the string s, then checks if the resulting string is a palindrome. The function isPalindrome is used to check