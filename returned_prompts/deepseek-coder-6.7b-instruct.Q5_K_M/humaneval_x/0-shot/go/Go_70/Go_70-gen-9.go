This solution works by first sorting the input list. It then creates a new list of the same length, and fills it with the elements from the input list, alternating between the smallest and largest remaining elements.

Here's a breakdown of how it works:
1. The input list is sorted in ascending order.
2. A new list, result, is created to hold the output.
3. The length of the input list is divided by 2 and the result list is filled with elements from the input list.
   For each i, result[i*2] is set to lst[i] (the i-th smallest element), and result[i*2+1] is set to lst[len(lst)-i-1] (the i-th largest element).
4. The result list is returned.

This solution has a time complexity of O(n log n) due to the sorting operation, and a space complexity of O(n) for the result list.

Note: This solution assumes that the input list contains distinct elements. If the input list can contain duplicate elements, the solution will not work correctly.
*/



package main

import (
	"fmt"
)

func StrangeSortList(lst []int) []int {
	sort.Ints(lst)
	result := make([]int, len(lst))
	for i := 0; i < len(lst)/2; i++ {
		result[i*2] = lst[i]
		result[i*2+1] = lst[len(lst)-i-1]
	}
	return result
}

func main() {
	fmt.Println(StrangeSortList([]int{1, 2, 3, 4})) // [1, 4, 2, 3