Here is the solution to the problem:
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
		// If the length of the list is even, the median is the average of the two middle numbers
		mid1 := l[n/2 - 1]
		mid2 := l[n/2]
		return float64(mid1+mid2) / 2
	} else {
		// If the length of the list is odd, the median is the middle number
		return float64(l[n/2])
	}
}
```
Explanation:

*   The `sort.Ints` function is used to sort the list in ascending order.
*   The length of the list is calculated using the `len` function.
*   If the length of the list is even, the median is calculated as the average of the two middle numbers. The middle numbers are accessed using the indices `n/2 - 1` and `n/2`.
*   If the length of the list is odd, the median is calculated as the middle number, which is accessed using the index `n/2`.
*   The median is returned as a floating-point number.

Note: This solution assumes that the input list is non-empty. If the input list is empty, the function will panic when trying to access the first element of the list. You may want to add a check for this case and return an error or a special value (e.g., NaN) to indicate that the input list is empty.