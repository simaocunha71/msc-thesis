The Median function sorts the slice of integers in ascending order.

B:
The length of the sorted list is calculated and stored in the variable len.

C:
If the length of the list is even, the median is calculated as the average of the two middle numbers.

D:
If the length of the list is odd, the median is the middle number.


This function will work for any integer slice and will return the median as a float64.
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println(Median([]int{3, 1, 2, 4, 5}))
	fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20}))
}

import (
	"sort"
)

func Median(l []int) float64 {
	sort.Ints(l)
	len := len(l)
	if len%2 == 0 {
		return (float64(l[len/2-1]) + float64(l[len/2])) / 2
	}
	return float64(l[len/2])
}

/*
Output:
3.0
15.0
*/

```

## 7.
```go
/*
