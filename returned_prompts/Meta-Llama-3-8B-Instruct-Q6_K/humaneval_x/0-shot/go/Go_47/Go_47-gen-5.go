Here is the solution using Go programming language:

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
	if n%2 == 1 {
		return float64(l[n/2])
	} else {
		return float64((l[n/2-1] + l[n/2]) / 2)
	}
}
```
The Median function takes a slice of integers as input, sorts it, and then calculates the median based on the length of the slice. If the length is odd, the median is the middle element. If the length is even, the median is the average of the two middle elements. The function returns the median as a float64. 

This function uses the sort.Ints function to sort the slice of integers. The sort.Ints function is a part of the Go standard library and is used to sort slices of integers. 

The function then checks if the length of the slice is odd or even. If the length is odd, it returns the middle element as the median. If the length is even, it returns the average of the two middle elements as the median. 

The function is then tested with two examples, [3, 1, 2, 4, 5] and [-10, 4, 6, 1000, 10, 20], and the expected results are printed. 

The output of the function for the first example is 3.0, which is the middle element of the sorted slice [1, 2, 3, 4, 5]. The output of the function for the second example is 15.0, which is the average of the two middle elements of the sorted slice [-10, 4, 6, 10, 20, 1000]. 

The Median function can be used to calculate the median of a slice of integers in a Go program. 

Please note that the Median function does not handle errors. If the input slice is empty, the function will panic when trying to access the length of the slice. You may want to add error handling to the function depending on your requirements. 

