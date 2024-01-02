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
	n := len(l)
	if n%2 == 0 {
		return l
	}
	left := make([]int, n/2)
	right := left[len(left)-1:] // make it easier to read with shorter variable names
	copy(left, right[:])
	sort.Ints(left)

	for i, j := 0, len(l)/2-1; i < n/2 && j >= 0; i++ {
		if l[i] == l[j+n%2] {
			left[i], left[j+n%2] = l[j+n%2], l[i]
		} else if l[i] > l[j+n%2] {
			right = append(right, l[j])
			right = append(right, left...)
			left = make([]int, n/2)
			copy(left, right[:])
		} else {
			left = append(left, l[i])
			left = append(left, l[j])
			right = left[len(left)-1:] // make it easier to read with shorter variable names
			copy(left, right[:])
		}
	}

	return []int{l[0], ...left}
}
