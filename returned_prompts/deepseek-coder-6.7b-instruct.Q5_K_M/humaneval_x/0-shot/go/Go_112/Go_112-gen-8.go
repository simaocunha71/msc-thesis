    str := strings.Map(func(r rune) rune {
        if strings.ContainsRune(c, r) {
            return -1
        }
        return r
    }, s)
    str = strings.ReplaceAll(str, " ", "")
    isPalindrome := str == Reverse(str)
    return [2]interface{}{str, isPalindrome}
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}


In the code above, we are using Map function of the strings package to map each rune in string s to its corresponding rune if it is not present in string c. If it is present, we map it to -1 which is not a valid rune and we don't include it in the result string.
After that we are replacing all spaces in the string with nothing and check if the result string is palindrome by comparing it with its reverse.
Finally, we return the result string and the boolean value indicating whether the string is palindrome.
*/

package main

import (
	"fmt"
	"strings"
)

func ReverseDelete(s, c string) [2]interface{} {
	str := strings.Map(func(r rune) rune {
		if strings.ContainsRune(c, r) {
			return -1
		}
		return r
	}, s)
	str = strings.ReplaceAll(str, " ", "")
	isPalindrome := str == Reverse(str)
	return [2]interface{}{str, isPalindrome}
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes