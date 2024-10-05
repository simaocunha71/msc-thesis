
}
*/

package main

import (
	"fmt"
	"strings"
)

func SameChars(s0 string, s1 string) bool {

	counts0 := make(map[rune]int)
	counts1 := make(map[rune]int)

	for _, c := range s0 {
		counts0[c]++
	}
	for _, c := range s1 {
		counts1[c]++
	}

	if len(counts0) != len(counts1) {
		return false
	}

	for k, v := range counts0 {
		if counts1[k] != v {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
	fmt.Println(SameChars("abcd", "dddddddabc"))               // true
	fmt.Println(SameChars("dddddddabc", "abcd"))               // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))              // false
	fmt.Println(SameChars("abcd", "dddddddabce"))              // false
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))   // false
}
