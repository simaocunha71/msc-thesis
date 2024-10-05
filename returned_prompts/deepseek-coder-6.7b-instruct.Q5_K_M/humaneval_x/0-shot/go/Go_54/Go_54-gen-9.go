
// Sort the strings.
sort.Slice(s0, func(i, j int) bool { return s0[i] < s0[j] })
sort.Slice(s1, func(i, j int) bool { return s1[i] < s1[j] })

// Compare the sorted strings.
return s0 == s1
}

func main() {

B:

fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
fmt.Println(SameChars("abcd", "dddddddabc")) // true
fmt.Println(SameChars("dddddddabc", "abcd")) // true
fmt.Println(SameChars("eabcd", "dddddddabc")) // false
fmt.Println(SameChars("abcd", "dddddddabce")) // false
fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc")) // false
}
```

This code sorts the characters in each string and then checks if the sorted strings are equal. If they are, it returns `true`, indicating that the strings contain the same characters in the same amount. If they are not equal, it returns `false`.

This code runs in O(n log n) time, where n is the length of the string, because it sorts the strings. It also uses O(n) space for the sorted strings.
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
	fmt.Println(SameChars("ab