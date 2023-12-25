import (
	"sort"
)

// This function takes a list l and returns a list l' such that
// l' is identical to l in the odd indicies, while its values at the even indicies are equal
// to the values of the even indicies of l, but sorted.
// >>> SortEven([1, 2, 3])
// [1, 2, 3]
// >>> SortEven([5, 6, 3, 4])
// [3, 6, 5, 4]
func SortEven(l []int) []int {
	even := make([]int, len(l))
	copy(even[0:], l[:]) // copy the list to even.

	for i := range l {
		if i%2 == 1 {
			even[i/2] = even[i/2-1] + l[i]
		} else {
			even[i/2] = even[i/2] + l[i]
		}
	}
	return append(l[:], even...) // return the sorted list.
}