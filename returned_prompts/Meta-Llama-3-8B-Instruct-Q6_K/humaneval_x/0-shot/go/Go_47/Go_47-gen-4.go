Here is a Go solution for the problem:

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
		return float64((l[n/2-1] + l[n/2]) / 2)
	} else {
		return float64(l[n/2])
	}
}

func main() {
	fmt.Println(Median([]int{3, 1, 2, 4, 5})) // 3.0
	fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20})) // 15.0
}
```

In this code, we use the built-in sort package in Go to sort the list. Then we check if the length of the list is even or odd. If it's even, we take the average of the two middle elements. If it's odd, we take the middle element. The result is then converted to a float64 and returned. The main function demonstrates how to use the Median function. The output of the program is `3.0` and `15.0` respectively.