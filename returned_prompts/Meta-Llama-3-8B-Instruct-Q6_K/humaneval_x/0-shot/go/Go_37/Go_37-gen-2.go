Here is the solution in Go:
```go
import (
	"sort"
)

func SortEven(l []int) []int {
	evenIndices := make([]int, 0, len(l)/2)
	for i := 0; i < len(l); i += 2 {
		evenIndices = append(evenIndices, l[i])
	}
	sort.Ints(evenIndices)
	result := make([]int, 0, len(l))
	for i := 0; i < len(l); i++ {
		if i%2 == 0 {
			result = append(result, evenIndices[i/2])
		} else {
			result = append(result, l[i])
		}
	}
	return result
}
```
This function first creates a slice of the even indices of the input slice `l`. Then, it sorts this slice using the `sort.Ints` function. Finally, it creates a new slice `result` by alternating between the sorted even indices and the original values of `l`. The `result` slice is then returned.

For example, if you call `SortEven([5, 6, 3, 4])`, the function will return `[3, 6, 5, 4]`, which is the original slice with the even indices sorted.