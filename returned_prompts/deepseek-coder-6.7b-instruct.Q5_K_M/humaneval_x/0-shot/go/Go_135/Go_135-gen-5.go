
// Write your solution here

}

*/

import (
	"sort"
)

func CanArrange(arr []int) int {
	sort.Ints(arr)
	for i := len(arr) - 1; i > 0; i-- {
		if arr[i] < arr[i-1] {
			return i
		}
	}
	return -1
}

// end

/*

