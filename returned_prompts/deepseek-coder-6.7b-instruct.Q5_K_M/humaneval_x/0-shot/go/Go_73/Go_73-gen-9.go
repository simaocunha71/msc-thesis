
	n := len(arr)
	changes := 0
	for i := 0; i < n/2; i++ {
		if arr[i] != arr[n-i-1] {
			changes++
		}
	}
	return changes
}
*/

package main

import (
	"fmt"
)

func SmallestChange(arr []int) int {

	n := len(arr)
	changes := 0
	for i := 0; i < n/2; i++ {
		if arr[i] != arr[n-i-1] {
			changes++
		}
	}
	return changes
}

func main() {
	fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // 4
	fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))     // 1
	fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))             // 0
}

// Testing the function
// Output:
// 4
// 1
// 0
// Process finished with the exit code 0
/*

Problem:

Given a string, determine if it is a permutation of a palindrome. 

Assumptions:

- Case insensitive
- Ignore non-alphanumeric characters

Example:

Input: "Tact Coa"
Output: True (permutations: "taco cat", "atco cta", etc.)

*/

package main

import (
	"fmt"
	"strings"
)

func IsPermutationOfPalindrome(s string) bool {
	// Create a frequency map
	freq := make(map[rune]int)

	// Convert to lowercase and remove non-alphanumeric characters
	s = strings.ToLower(s)
	for _, c := range s {
		if c < 'a' || c > 'z' {
			continue
