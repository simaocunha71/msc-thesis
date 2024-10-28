
// Your code goes here

}

*/

import (
	"strings"
)

func CycpatternCheck(a, b string) bool {

	for i := 0; i < len(b); i++ {
		if strings.Contains(a, b) {
			return true
		}
		b = b[1:] + string(b[0])
	}
	return false
}

// In the main function, call the CycpatternCheck function with the words you want to check.
func main() {

	println(CycpatternCheck("abcd", "abd"))
	println(CycpatternCheck("hello", "ell"))
	println(CycpatternCheck("whassup", "psus"))
	println(CycpatternCheck("abab", "baa"))
	println(CycpatternCheck("efef", "eeff"))
	println(CycpatternCheck("himenss", "simen"))
}

// CycpatternCheck function checks if the string b or any of its rotations are a substring in the string a.
// It uses a for loop to rotate the string b and checks if it is a substring of a.
// If any rotation of b is a substring of a, the function returns true.
// If no rotation of b is a substring of a after the loop, the function returns false.
// The function uses the strings.Contains function to check if a substring is a substring of a.
// The function returns a boolean value indicating whether b or any of its rotations is a substring of a.
// The time complexity of the function is O(n^2) because of the contains function in the loop.
// The space complexity is O(n) because of the creation of a new string in each iteration of the loop.
