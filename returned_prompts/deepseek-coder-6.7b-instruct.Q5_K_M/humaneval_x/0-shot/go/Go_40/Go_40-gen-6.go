
  // Your solution here

}

*/

package main

import (
	"fmt"
	"sort"
)

func TriplesSumToZero(l []int) bool {

	sort.Ints(l)

	for i := 0; i < len(l)-2; i++ {
		start := i + 1
		end := len(l) - 1
		for start < end {
			sum := l[i] + l[start] + l[end]
			if sum == 0 {
				return true
			} else if sum < 0 {
				start += 1
			} else {
				end -= 1
			}
		}
	}

	return false
}

func main() {
	fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7}))
	fmt.Println(TriplesSumToZero([]int{1}))
}
package main

import (
	"fmt"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	maxA, left, right := 0, 0, len(height)-1
	for left < right {
		maxA = max(maxA, min(height[left], height[right])*(right-left))
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return maxA
}

func main() {
	height := []int{1, 8,