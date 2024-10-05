
// Initialize two pointers, one at the start of the string, and one at the end of the string
start := 0
end := len(text) - 1

// Loop while the start pointer is less than the end pointer
for start < end {

    // If the characters at the start and end pointers are not equal, return false
    if text[start] != text[end] {
        return false
    }

    // Otherwise, increment the start pointer and decrement the end pointer
    start++
    end--
}

// If we got this far, the string is a palindrome, so return true
return true

}
*/

package main

import (
	"fmt"
)

func IsPalindrome(text string) bool {
	start := 0
	end := len(text) - 1

	for start < end {
		if text[start] != text[end] {
			return false
		}
		start++
		end--
	}
	return true
}

func main() {
	fmt.Println(IsPalindrome(""))         // true
	fmt.Println(IsPalindrome("aba"))      // true
	fmt.Println(IsPalindrome("aaaaa"))    // true
	fmt.Println(IsPalindrome("zbcd"))     // false
	fmt.Println(IsPalindrome("abcdcba"))  // true
	fmt.Println(IsPalindrome("abcddcba")) // true
}
package main

import "fmt"

func FindTwoElementsSumToTarget(arr []int, target int) []int {
	seen := make(map[int]bool)
	for _, num := range arr {
		potentialMatch := target - num
		if seen[potentialMatch] {
			return []int{potentialMatch, num}
		}
		seen[num] = true
	}
	return []int{}
}

func main() {
	fmt.Println(FindTwoElementsSumToTarget([]int{3, 5, -4, 8, 11,