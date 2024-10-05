
// 1st: Check if the length of the second word is larger than the first. If so, return false.
    if len(b) > len(a) {
        return false
    }

// 2nd: Create a variable to store the length of the second word.
    lenB := len(b)

// 3rd: Create a variable to store the length of the first word.
    lenA := len(a)

// 4th: Create a variable to store the result.
    res := false

// 5th: Use a for loop to check all the rotations.
    for i := 0; i < lenB; i++ {

// 6th: Create a variable to store the rotation.
        rot := b[lenB-i:] + b[:lenB-i]

// 7th: Check if the rotation is a substring in the first word.
        if strings.Contains(a, rot) {
            res = true
            break
        }
    }

// 8th: Return the result.
    return res
}

*/

package main

import (
	"fmt"
	"strings"
)

func CycpatternCheck(a, b string) bool {
	if len(b) > len(a) {
		return false
	}
	lenB := len(b)
	lenA := len(a)
	res := false
	for i := 0; i < lenB; i++ {
		rot := b[lenB-i:] + b[:lenB-i]
		if strings.Contains(a, rot) {
			res = true
			break
		}
	}
	return res
}

func main() {
	fmt.Println(CycpatternCheck("abcd", "abd"))
	fmt.Println(CycpatternCheck("hello", "ell"))
	fmt.Println(CycpatternCheck("whassup", "psus"))
	fmt.Println(CycpatternCheck("abab", "baa"))
	fmt.Println(CycpatternCheck("efef", "eeff"))
	f