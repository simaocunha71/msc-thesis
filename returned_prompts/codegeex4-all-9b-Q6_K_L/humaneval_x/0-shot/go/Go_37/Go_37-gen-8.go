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
	var evenIndicies []int
	for i := 0; i < len(l); i += 2 {
		evenIndicies = append(evenIndicies, l[i])
	}
	sort.Ints(evenIndicies)
	for i := 0; i < len(evenIndicies); i += 2 {
		l[i] = evenIndicies[i]
	}
	return l
}