```
package main

import (
	"fmt"
	"sort"
)

func PairsSumToZero(l []int) bool {
	sort.Ints(l)
	var left, right int
	for left < right {
		sum := l[left] + l[right]
		if sum == 0 {
			return true
		} else if sum < 0 {
			left++
		} else {
			right--
		}
	}
	return false
}

func main() {
	fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(PairsSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7}))
	fmt.Println(PairsSumToZero([]int{1}))
}
```

The two-pointer technique is used to solve this problem. It's a common technique used to solve problems that involve finding pairs of elements in a list that satisfy a certain condition.

Here's how it works:

1. First, we sort the list. This is because we want to be able to easily find pairs of elements that sum to zero.
2. We then initialize two pointers, `left` and `right`, to the start and end of the list, respectively.
3. We then enter a loop that continues until `left` is no longer less than `right`.
4. Inside the loop, we calculate the sum of the elements at the `left` and `right` indices.
5. If the sum is zero, we return `true`, indicating that we've found a pair of elements that sum to zero.
6. If the sum is less than zero, we increment `left` to move the `left` pointer to the right.
7. If the sum is greater than zero, we decrement `right` to move the `right` pointer to the left.
8. If the loop completes without finding a pair of elements that sum to zero, we return `false`.

This technique has a time complexity of O(n log n) due to the sorting, where n is the length of the list. It has a space complexity of O(1) because we only use a constant amount of space to store the pointers and the sum.