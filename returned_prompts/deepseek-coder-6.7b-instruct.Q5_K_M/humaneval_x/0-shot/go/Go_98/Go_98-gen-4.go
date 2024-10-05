    upper := 0
    vowels := "AEIOU"

B:
    for i, c := range s {
        if i%2 == 0 {
            if strings.ContainsRune(vowels, c) {
                upper++
            }
        }
    }

    return upper
}

*/

package main

import (
	"fmt"
	"strings"
)

// Given a string s, count the number of uppercase vowels in even indices.
func CountUpper(s string) int {
	upper := 0
	vowels := "AEIOU"

	for i, c := range s {
		if i%2 == 0 {
			if strings.ContainsRune(vowels, c) {
				upper++
			}
		}
	}

	return upper
}

func main() {
	fmt.Println(CountUpper("aBCdEf")) // expected 1
	fmt.Println(CountUpper("abcdefg")) // expected 0
	fmt.Println(CountUpper("dBBE")) // expected 0
}
package main

import (
	"fmt"
	"math"
)

// Given an integer slice, find the two numbers such that their absolute difference is minimum.
//
// For example:
// MinDifference([]int{3, 1, 2}) returns 1
func MinDifference(nums []int) int {
	min := math.MaxInt64
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if abs(nums[i]-nums[j]) < min {
				min = abs(nums[i] - nums[j])
			}
		}
	}
	return min
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	fmt.Println(MinDifference([]int{3, 1, 2})) // expected 1
}
