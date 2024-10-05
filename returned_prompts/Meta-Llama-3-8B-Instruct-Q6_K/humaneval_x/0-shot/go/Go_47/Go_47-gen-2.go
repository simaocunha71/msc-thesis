Here is a simple solution in Go:
```go
import (
	"sort"
)

func Median(l []int) float64 {
	sort.Ints(l)
	n := len(l)
	if n%2 == 1 {
		return float64(l[n/2])
	} else {
		mid1 := l[n/2 - 1]
		mid2 := l[n/2]
		return float64((mid1 + mid2) / 2)
	}
}
```
Explanation:

1. First, we sort the list `l` in ascending order using the `sort.Ints` function from the `sort` package.
2. Then, we find the length `n` of the sorted list.
3. If the length `n` is odd, the median is the middle element, which we can access using `l[n/2]`.
4. If the length `n` is even, the median is the average of the two middle elements, which we can access using `l[n/2-1]` and `l[n/2]`.
5. We convert the median to a `float64` value and return it.

You can test this function with the examples you provided:
```go
fmt.Println(Median([]int{3, 1, 2, 4, 5})) // Output: 3.0
fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20})) // Output: 15.0
```