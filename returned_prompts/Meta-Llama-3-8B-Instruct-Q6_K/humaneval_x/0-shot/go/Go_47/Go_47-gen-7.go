Here is the solution to the problem:

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
	if n%2 == 1 {
		return float64(l[n/2])
	} else {
		return float64((l[n/2-1] + l[n/2]) / 2)
	}
}

func main() {
	fmt.Println(Median([]int{3, 1, 2, 4, 5})) // Output: 3
	fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20})) // Output: 15
}
```



The median of a list of numbers is the middle value of the list when it is sorted. If the list has an even number of elements, the median is the average of the two middle values.

The function `Median(l []int)` takes a slice of integers as input, sorts it, and then returns the median value.

In the `main` function, we test the `Median` function with two lists and print the results.

The time complexity of the `Median` function is O(n log n) due to the sorting operation. The space complexity is O(1) as we only use a constant amount of space to store the result.