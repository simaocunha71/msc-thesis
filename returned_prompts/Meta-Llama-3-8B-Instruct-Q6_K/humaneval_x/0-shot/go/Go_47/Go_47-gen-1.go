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
		median := float64((l[n/2-1] + l[n/2]) / 2)
		return median
	} else {
		return float64(l[n/2])
	}
}
```


In this code, we sort the list using the `sort.Ints` function, then check if the length of the list is even or odd. If the length is even, we calculate the median as the average of the two middle numbers. If the length is odd, we simply return the middle number. We convert the result to a float64 value to ensure the return type is consistent with the problem description.