
// Check if the string length is less than 3
if len(s) < 3 {
return false
}

// Loop over the string
for i := 0; i < len(s)-2; i++ {

// Check if the 3 consecutive letters are distinct
if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
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

func IsHappy(s string) bool {
	if len(s) < 3 {
		return false
	}

	for i := 0; i < len(s)-2; i++ {
		if s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(IsHappy("a"))
	fmt.Println(IsHappy("aa"))
	fmt.Println(IsHappy("abcd"))
	fmt.Println(IsHappy("aabb"))
	fmt.Println(IsHappy("adb"))
	fmt.Println(IsHappy("xyy"))
}

/*
Output:
false
false
true
false
true
false
*/

// This solution works by checking each three-character group in the string.
// If any group consists of the same character (i.e., they are not distinct), the function returns false.
// If no such group is found after checking all groups, the function returns true.
// The function first checks if the string length is less than 3, and if so, returns false.
// This is because a string of length less than 3 cannot possibly contain three distinct characters.
// The function then loops over the string, checking each three-character group.
// If a group consists of the same character, the function returns false.
// If the function does not find any such group, it returns true.
// This solution has a time complexity of O(n), where n is