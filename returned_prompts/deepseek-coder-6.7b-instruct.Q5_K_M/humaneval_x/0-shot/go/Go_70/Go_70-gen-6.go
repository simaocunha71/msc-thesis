    // First, let's handle the edge case of an empty list
    if len(lst) == 0 {
        return []int{}
    }

    // Next, we'll sort the list
    sort.Ints(lst)

    // We'll create a new list to hold the final result
    result := make([]int, len(lst))

    // We'll loop through the list, alternating between the minimum and maximum
    for i := 0; i < len(lst)/2; i++ {
        result[i*2] = lst[i]
        result[i*2+1] = lst[len(lst)-i-1]
    }

    // If the list length is odd, the middle element goes in the last position
    if len(lst)%2 != 0 {
        result[len(lst)-1] = lst[len(lst)/2]
    }

    // Finally, we return the result
    return result
}

The complexity of this solution is O(n log n) due to the sorting operation, which is necessary to solve this problem. The rest of the operations are O(n).

*/

package main

import (
	"fmt"
	"sort"
)

// StrangeSortList - given a list of integers, return the list sorted in a strange order.
func StrangeSortList(lst []int) []int {
	// handle edge case of empty list
	if len(lst) == 0 {
		return []int{}
	}

	// sort the list
	sort.Ints(lst)

	// create a new list to hold the final result
	result := make([]int, len(lst))

	// loop through the list, alternating between the minimum and maximum
	for i := 0; i < len(lst)/2; i++ {
		result[i*2] = lst[i]
		result[i*2+1] = lst[len(lst)-i-1]
	}

	// if the list length is odd, the middle element goes in the last position
	if len(lst)%2 !