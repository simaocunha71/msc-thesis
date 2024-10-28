Here is the solution:
```go
import (
	"sort"
)

func SortEven(l []int) []int {
	sort.Slice(l[1::2], func(i, j int) bool {
		return l[2*i+1] < l[2*j+1]
	})
	return l
}
```
Explanation:
The `SortEven` function takes a slice of integers `l` as input and returns a new slice that is identical to `l` in the odd indicies, while its values at the even indicies are equal to the values of the even indicies of `l`, but sorted.

We use the `sort.Slice` function to sort the slice of integers at the even indicies. The slice is defined as `l[1::2]`, which means we start from the second element (index 1) and go to the end of the slice, stepping by 2 each time.

The sorting function takes two indices `i` and `j` as input and returns a boolean indicating whether the element at index `2*i+1` is less than the element at index `2*j+1`. This is used to sort the slice in ascending order.

Finally, we return the modified slice. Note that we do not modify the original slice, but return a new slice with the desired properties. This is because the `sort.Slice` function modifies the slice in place, and we want to preserve the original slice.