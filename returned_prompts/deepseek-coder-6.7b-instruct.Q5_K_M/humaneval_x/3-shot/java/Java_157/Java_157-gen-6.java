
}

*/

import (
	"math"
)

func IsSimplePower(x int, n int) bool {
	if x == 1 {
		return true
	}
	if n <= 1 || x <= 0 {
		return false
	}

	val := math.Log(float64(x)) / math.Log(float64(n))

	return math.Floor(val) == math.Ceil(val)
}

// End

/*

// Test Cases

func main() {
	fmt.Println(IsSimplePower(1, 4)) // => true
	fmt.Println(IsSimplePower(2, 2)) // => true
	fmt.Println(IsSimplePower(8, 2)) // => true
	fmt.Println(IsSimplePower(3, 2)) // => false
	fmt.Println(IsSimplePower(3, 1)) // => false
	fmt.Println(IsSimplePower(5, 3)) // => false
}

*/
// Test Cases
package main

import (
	"fmt"
	"sort"
	"strings"
)

func FindShortest(s string) string {
	subStrings := make(map[string]bool)
	words := strings.Fields(s)

	for _, word := range words {
		for i := 0; i < len(word); i++ {
			for j := i + 1; j <= len(word); j++ {
				subStrings[word[i:j]] = true
			}
		}
	}

	keys := make([]string, 0, len(subStrings))
	for key := range subStrings {
		keys = append(keys, key)
	}

	sort.Slice(keys, func(i, j int) bool {
		if len(keys[i]) == len(keys[j]) {
			return keys[i] < keys[j]
		}
		return len(keys[i]) < len(keys[j])
	})

	for _, key := range keys {
		if len(key) !=