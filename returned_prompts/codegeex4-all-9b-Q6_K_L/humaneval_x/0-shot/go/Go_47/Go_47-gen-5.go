import (
	"sort"
	"reflect"
)

// Return Median of elements in the list l.
// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
func Median(l []int) float64 {
	sort.Slice(l, func(i, j int) bool {
		return l[i] < l[j]
	})
	mid := len(l) / 2
	if len(l) % 2 == 0 {
		return float64(l[mid-1] + l[mid]) / 2
	}
	return float64(l[mid])
}

// >>> Median([3, 1, 2, 4, 5])
// 3.0
// >>> Median([-10, 4, 6, 1000, 10, 20])
// 15.0
// >>> Median([-10, 4, 6, 1000, 10, 20, 0])
// 10.0
// >>> Median([-10, 4, 6, 1000, 10])
// 7.0
// >>> Median([-10, 4, 6, 1000])
// 6.0
// >>> Median([-10, 4, 6])
// 4.0
// >>> Median([-10, 4])
// -2.0
// >>> Median([-10])
// -10.0
// >>> Median([-10, 4, 6, 1000, 10, 20, 0, 5, 8, 7, 9, 1])
// 6.0
// >>> Median([-10, 4, 6, 1000, 10, 20, 0, 5, 8, 7, 9, 1, 3])
// 5.0
// >>> Median([-10, 4, 6, 1000, 10, 20, 0, 5, 8, 7, 9, 1, 3, 2])
// 5.0
// >>> Median([-10, 4, 6, 1000, 10, 20, 0, 5, 8, 7, 9, 