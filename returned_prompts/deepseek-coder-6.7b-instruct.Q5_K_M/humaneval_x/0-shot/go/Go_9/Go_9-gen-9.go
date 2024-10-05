    maxs := make([]int, len(numbers))
    max := math.MinInt64
    for i, number := range numbers {
        if number > max {
            max = number
        }
        maxs[i] = max
    }
    return maxs
}

*/

package main

import (
	"fmt"
)

func RollingMax(numbers []int) []int {
	maxs := make([]int, len(numbers))
	max := numbers[0]
	for i, number := range numbers {
		if number > max {
			max = number
		}
		maxs[i] = max
	}
	return maxs
}

func main() {
	numbers := []int{1, 2, 3, 2, 3, 4, 2}
	maxs := RollingMax(numbers)
	fmt.Println(maxs)
}

// Output:
// [1 2 3 3 3 4 4]
package main

import (
	"fmt"
	"math"
)

func max(x int, y int) int {
	if x < y {
		return y
	}
	return x
}

func lengthOfLongestSubstring(s string) int {
	n := len(s)
	ans := 0
	i := 0
	m := make(map[rune]int)
	for j := 0; j < n; j++ {
		r := rune(s[j])
		if _, ok := m[r]; ok {
			i = max(m[r], i)
		}
		ans = max(ans, j-i+1)
		m[r] = j + 1
	}
	return ans
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
	fmt.Println(lengthOfLongestSubstring("bbbbbb"))
	fmt.Println(lengthOfLongestSubstring("pwwkew"))
	fmt.Println(length