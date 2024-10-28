import (
	"sort"
)

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []int) float64 {
	sort.Ints(l)
	median := float64(l[len(l)/2])
	if len(l)%2 == 0 {
		median = (median + float64(l[len(l)/2-1])) / 2
	}
	return median
}
