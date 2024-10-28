    sort.Ints(l1)
    sort.Ints(l2)

B:
    var common []int
    i, j := 0, 0

C:
    for i < len(l1) && j < len(l2) {
        if l1[i] < l2[j] {
            i++
        } else if l1[i] > l2[j] {
            j++
        } else {
            common = append(common, l1[i])
            i++
            j++
        }
    }

    return common
}

The function works by first sorting both input slices. It then iterates through both slices simultaneously, comparing the elements at each index. If the elements are equal, the element is added to the result slice and both indices are incremented. If the element in the first slice is smaller, the first slice index is incremented; if the element in the second slice is smaller, the second slice index is incremented.

The time complexity of the function is O(n log n) due to the sorting, where n is the length of the longest slice. The space complexity is O(k), where k is the number of common elements between the two slices.
*/
package main

import (
	"fmt"
)

func Common(l1 []int, l2 []int) []int {
	sort.Ints(l1)
	sort.Ints(l2)

	var common []int
	i, j := 0, 0

	for i < len(l1) && j < len(l2) {
		if l1[i] < l2[j] {
			i++
		} else if l1[i] > l2[j] {
			j++
		} else {
			common = append(common, l1[i])
			i++
			j++
		}
	}

	return common
}

func main() {
	fmt.Println(Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 6