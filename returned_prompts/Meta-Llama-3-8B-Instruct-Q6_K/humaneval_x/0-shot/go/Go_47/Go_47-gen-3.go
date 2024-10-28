Here is the solution:

```go
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
	n := len(l)
	if n%2 == 0 {
		median := (l[n/2-1] + l[n/2]) / 2
		return float64(median)
	} else {
		return float64(l[n/2])
	}
}
```

Explanation:
This function sorts the input list `l` and then finds the median. If the length of the list is even, the median is the average of the two middle numbers. If the length of the list is odd, the median is the middle number.

The time complexity of this function is O(n log n) due to the sorting operation, where `n` is the length of the input list. The space complexity is O(1) as we are using a constant amount of space to store the result. 