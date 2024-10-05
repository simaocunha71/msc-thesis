import (
	"sort"
)

// This function takes a list l and returns a list l' such that
// l' is identical to l in the odd indicies, while its values at the even indicies are equal
// to the values of the even indicies of l, but sorted.
func SortEven(l []int) []int {
	even := make([]int, 0)
	for i, n := range l {
		if i%2 == 0 {
			even = append(even, n)
		}
	}
	sort.Ints(even)
	for i, n := range even {
		l[i*2] = n
	}
	return l
}