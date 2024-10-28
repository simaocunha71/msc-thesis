Here is the solution:
```go
func SortEven(l []int) []int {
    sort.Slice(l[1::2], func(i, j int) bool { return l[2*i+1] < l[2*j+1] })
    return l
}
```
Explanation:

*   The `sort.Slice` function is used to sort the slice `l[1::2]`, which represents the even indices of the original slice `l`.
*   The sorting is done based on the values at the odd indices of the original slice, accessed using the expression `l[2*i+1]`.
*   The sorted slice is then returned.

You can test this function using the following code:
```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(SortEven([]int{1, 2, 3}))  // [1, 2, 3]
	fmt.Println(SortEven([]int{5, 6, 3, 4})) // [3, 6, 5, 4]
}
```  