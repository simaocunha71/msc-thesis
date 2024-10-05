You are correct. To implement the Median function in Go, you need to sort the slice and then return the middle element(s). If the slice has an odd number of elements, return the middle one. If it has an even number, return the average of the two middle elements. Here is how you can do it:

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
	if n%2 == 1 { // Odd number of elements
		return float64(l[n/2])
	} else { // Even number of elements
		return (float64(l[n/2-1]) + float64(l[n/2])) / 2
	}
}
```

In the code above, we use the sort.Ints function from the sort package to sort the slice. Then, we check if the number of elements is odd or even. If it's odd, we return the middle element. If it's even, we return the average of the two middle elements.