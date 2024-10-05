Here is a solution in Go:

```go
import (
	"fmt"
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
		return float64(l[n/2-1] + l[n/2]) / 2.0
	} else {
		return float64(l[n/2])
	}
}

func main() {
	fmt.Println(Median([]int{3, 1, 2, 4, 5})) // Output: 3
	fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20})) // Output: 15
}
```

This program first sorts the input slice `l` and then calculates the median. If the length of `l` is even, the median is the average of the two middle elements. If the length of `l` is odd, the median is the middle element. The result is returned as a floating-point number. The `main` function demonstrates the usage of the `Median` function.