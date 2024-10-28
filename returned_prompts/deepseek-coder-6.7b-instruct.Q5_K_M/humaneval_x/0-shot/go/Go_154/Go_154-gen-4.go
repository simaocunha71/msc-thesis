
// You need to loop through all the rotations of the second word
for i := 0; i < len(b); i++ {

B:

// You need to check if the current rotation is a substring of the first word
if strings.Contains(a, b) {

C:

// If it is, return true
return true
}

D:

// If not, rotate the second word
b = b[len(b)-1:] + b[:len(b)-1]

E:

// Continue the loop
}

F:

// If after all rotations, no rotation is a substring, return false
return false
}
*/

package main

import (
	"fmt"
	"strings"
)

func CycpatternCheck(a, b string) bool {
	for i := 0; i < len(b); i++ {
		if strings.Contains(a, b) {
			return true
		}
		b = b[len(b)-1:] + b[:len(b)-1]
	}
	return false
}

func main() {
	fmt.Println(CycpatternCheck("abcd", "abd"))
	fmt.Println(CycpatternCheck("hello", "ell"))
	fmt.Println(CycpatternCheck("whassup", "psus"))
	fmt.Println(CycpatternCheck("abab", "baa"))
	fmt.Println(CycpatternCheck("efef", "eeff"))
	fmt.Println(CycpatternCheck("himenss", "simen"))
}

/*
Output:
false
true
false
true
false
true
*/

/*
This Go program works by looping through all the rotations of the second word (b) and checking if any of these rotations are substrings of the first word (a). If it finds a match, it returns true. If it doesn't find a match after checking all rotations, it returns false.
*/

/*
Note: The function strings.Contains() is used to check if a string contains a substring. The function strings.Contains(s, substring) returns