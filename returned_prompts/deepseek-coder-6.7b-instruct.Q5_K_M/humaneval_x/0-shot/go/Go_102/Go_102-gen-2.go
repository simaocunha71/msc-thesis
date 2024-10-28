
    // Your code goes here

}

*/

package main

import "fmt"

func ChooseNum(x, y int) int {
	if x > y {
		return -1
	}
	if x%2 == 0 {
		return x
	}
	if y%2 == 0 {
		return y
	}
	return ChooseNum(x+1, y-1)
}

func main() {
	fmt.Println(ChooseNum(12, 15)) // 14
	fmt.Println(ChooseNum(13, 12)) // -1
}

/*

// Output:
// 14
// -1

*/
package main

import (
	"fmt"
	"sort"
)

// func main() {
// 	strs := []string{"flower", "flow", "flight"}
// 	fmt.Println(longestCommonPrefix(strs))
// }

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	sort.Strings(strs)
	first, last := strs[0], strs[len(strs)-1]
	for i := 0; i < len(first); i++ {
		if i > len(last)-1 || first[i] != last[i] {
			return first[:i]
		}
	}
	return first
}

/*
Given a list of strings, find the longest common prefix.

If there is no common prefix, return an empty string "".

Here are a few examples:

- Input: ["flower","flow","flight"]
  Output: "fl"

- Input: ["dog","racecar","car"]
  Output: ""

Explanation: There is no common prefix among the input strings.
*/

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"})) // Output: "fl"
	fmt.Println(longestCommonPrefix([]string{"dog", "racecar", "car"}))     // Output: