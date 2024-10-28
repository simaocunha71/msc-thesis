```go
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
	var even []int
	for i, v := range l {
		if i%2 == 0 {
			even = append(even, v)
		}
	}
	sort.Ints(even)
	for i, v := range even {
		l[i*2] = v
	}
	return l
}
```