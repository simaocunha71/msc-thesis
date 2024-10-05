
	sort.Slice(s0, func(i, j int) bool { return s0[i] < s0[j] })
	sort.Slice(s1, func(i, j int) bool { return s1[i] < s1[j] })

B:

	return s0 == s1
}

func main() {

C:

	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
	fmt.Println(SameChars("abcd", "dddddddabc"))             // true
	fmt.Println(SameChars("dddddddabc", "abcd"))             // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))            // false
	fmt.Println(SameChars("abcd", "dddddddabce"))            // false
	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc")) // false
}
*/

package main

import (
	"fmt"
	"sort"
)

func SameChars(s0 string, s1 string) bool {

	sort.Slice(s0, func(i, j int) bool { return s0[i] < s0[j] })
	sort.Slice(s1, func(i, j int) bool { return s1[i] < s1[j] })

	return s0 == s1
}

func main() {

	fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
	fmt.Println(SameChars("abcd", "dddddddabc"))               // true
	fmt.Println(SameChars("dddddddabc", "abcd"))               // true
	fmt.Println(SameChars("eabcd", "dddddddabc"))              // false
	fmt.Println(SameChars("abcd", "dddddddabce"))              // false
	fmt.Println(SameChars("eab